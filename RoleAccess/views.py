from django.contrib import messages
from django.contrib.auth.models import Group, User

from .forms import AssignGroupForm
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.urls import reverse


class AssignGroupView(View):
    def get(self, request):
        user_ids = request.GET.getlist('user_id')
        roles = Group.objects.all()
        form = AssignGroupForm
        return render(
            request,
            "assign_group.html",
            {
                "form": form,
                "user_id": user_ids,
                "roles": roles
            },
        )

    def post(self, request):
        form = AssignGroupForm(request.POST)
        if form.is_valid():
            users = form.save()
            usernames = ', '.join([user.username for user in users])
            messages.success(request, f"The users '{usernames}' is assigned to the role.")
            # return redirect(reverse('admin:auth_user_change', args=(save.id,)) + '#permissions-tab')
            return redirect('/assign_group/')
        return redirect('your-failure-url')


class RemoveUserFromRoleView(View):
    def post(self, request):
        role_id = request.POST.get('role_id')
        user_id = request.POST.get('user_id')
        role = Group.objects.get(id=role_id)
        user = role.user_set.get(id=user_id)
        role.user_set.remove(user)
        messages.success(request, f"The user '{user.username}' has been removed from role '{role}'.")
        return redirect('/assign_group/')


from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User


def toggle_user_status(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        action = request.POST.get('action')  # 'activate' or 'deactivate'

        try:
            user = User.objects.get(id=user_id)
            if action == 'activate':
                user.is_staff = True
                user.save()
                return JsonResponse({'status': 'success', 'message': 'User activated successfully.'})
            elif action == 'deactivate':
                user.is_staff = False
                user.save()
                return JsonResponse({'status': 'success', 'message': 'User deactivated successfully.'})
            else:
                return JsonResponse({'status': 'error', 'message': 'Invalid action.'})
        except User.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'User does not exist.'})

    elif request.method == 'GET':
        # Assuming 'users' contains the queryset of all users
        users = User.objects.all()
        return render(request, 'toggle_user_status.html', {'users': users})

    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})


def user_detail(request, user_id):
    # Assuming User is your custom user model
    user = get_object_or_404(User, pk=user_id)
    url = reverse('admin:%s_%s_change' % (user._meta.app_label, user._meta.model_name), args=[user_id])
    return redirect(url)
