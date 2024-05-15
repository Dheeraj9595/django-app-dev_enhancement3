import yaml
import msal
import os
import time

# -------------------------Auth helper---------------------------------------------------------------------------


stream = open('oauth_settings.yml', 'r')
settings = yaml.load(stream, yaml.SafeLoader)


def load_cache(request):
    # Check for a token cache in the session
    cache = msal.SerializableTokenCache()
    if request.session.get('token_cache'):
        cache.deserialize(request.session['token_cache'])
    return cache


def save_cache(request, cache):
    # If cache has changed, persist back to session
    if cache.has_state_changed:
        request.session['token_cache'] = cache.serialize()


def get_msal_app(cache=None):
    # Initialize the MSAL confidential client
    auth_app = msal.ConfidentialClientApplication(
        settings['app_id'],
        authority=settings['authority'],
        client_credential=settings['app_secret'],
        token_cache=cache)
    return auth_app


# Method to generate a sign-in flow
def get_sign_in_flow():
    auth_app = get_msal_app()
    # breakpoint()
    return auth_app.initiate_auth_code_flow(
        settings['scopes'],
        redirect_uri=settings['redirect'])


# Method to exchange auth code for access token
def get_token_from_code(request):
    cache = load_cache(request)
    auth_app = get_msal_app(cache)

    # Get the flow saved in session
    flow = request.session.pop('auth_flow', {})
    print(request.GET)

    result = auth_app.acquire_token_by_auth_code_flow(flow, request.GET)
    save_cache(request, cache)

    return result


def store_user(request, user):
    try:
        request.session['user'] = {
            'is_authenticated': True,
            'name': user['displayName'],
            'email': user['mail'] if (user['mail'] != None) else user['userPrincipalName'],
            # 'timeZone': user['mailboxSettings']['timeZone'] if (user['mailboxSettings']['timeZone'] != None) else
            # 'UTC'
        }
    except Exception as e:
        print(e)


def get_token(request):
    cache = load_cache(request)
    auth_app = get_msal_app(cache)

    accounts = auth_app.get_accounts()
    if accounts:
        result = auth_app.acquire_token_silent(
            settings['scopes'],
            account=accounts[0])
        save_cache(request, cache)

        return result['access_token']


def remove_user_and_token(request):
    if 'token_cache' in request.session:
        del request.session['token_cache']

    if 'user' in request.session:
        del request.session['user']


# ----------------------------------------------------graph helper-----------------------------------------------

import requests
import json
from django.contrib.auth.models import User
from django.http import HttpResponseBadRequest
from django.shortcuts import redirect
from django.contrib.auth import login


def get_user_view(request):
    token = request.session.get('access_token')
    if token:
        user_data = fetch_user_data(token, request)
        if user_data:
            return redirect('http://localhost:3000/admin/')
    return HttpResponseBadRequest("Invalid credentials or token not found in cache.")


def fetch_user_data(token, request):
    # breakpoint()
    graph_endpoint = 'https://graph.microsoft.com/v1.0/me'
    headers = {
        'Authorization': 'Bearer ' + token
    }
    try:
        response = requests.get(graph_endpoint, headers=headers)
        response.raise_for_status()  # Raise an exception for bad responses
        user_data = response.json()
        # breakpoint()
        user_obj = User.objects.get(email=user_data['mail'])
        # Assuming `request` is available within the function
        login(request, user_obj, backend='django.contrib.auth.backends.ModelBackend')
        return user_data
    except Exception as e:
        # Handle any errors that occur during the API request
        print('Error fetching user data:', e)
        return None
