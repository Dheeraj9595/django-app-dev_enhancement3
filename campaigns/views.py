from django.views import View
from django.urls import reverse
from django.contrib import messages
from django.shortcuts import render, redirect

from RoleAccess.models import AccessTable
from backend.mixins import AdminLoginRequiredMixin, PermissionRequiredMixin, GroupRequiredMixin
from .forms import CampaignForm
import brands.models as brand_models
from products import models as product_models
from products.constants import CODE_POSITION_CHOICES
from analytics.constants import (
    CODE_TYPE_CHOICES,
    CODE_PLACEMENT_CHOICES,
)
from .models import CategoryUserLink


class CampaignFormView(AdminLoginRequiredMixin, GroupRequiredMixin, View):
    """
    A view for handling campaign form submissions.

    Inherits from Django's View class and requires admin login.

    Attributes:
        None
    """
    required_groups = ["Super Admin", "Client Admin User", "Campaign User"]

    # def get(self, request):
    #     """
    #     Handle GET request.
    #
    #     Retrieves data needed for rendering the campaign form and returns a response.
    #
    #     Args:
    #         request: HttpRequest object
    #
    #     Returns:
    #         HttpResponse object
    #     """
    #
    #     # Retrieve required data from models
    #     divisions = brand_models.Division.objects.filter(brand=None)
    #     local_brands = brand_models.LocalBrand.objects.all().exclude(brand=None)
    #     activities = product_models.Activity.objects.all()
    #     code_placement_choices = dict(CODE_POSITION_CHOICES)
    #     utm_source_choices = dict(CODE_PLACEMENT_CHOICES)
    #     utm_medium_choices = dict(CODE_TYPE_CHOICES)
    #     category_choices = dict(CATEGORY_CHOICES)
    #     # markets = product_models.Market.objects.all()
    #     product_objs = product_models.Product.objects.all()
    #     if request.user.groups.filter(name='Client Admin User').exists():
    #         # breakpoint()
    #         allowed_categories = CategoryUserLink.objects.filter(user=request.user).values_list('category', flat=True)
    #         category_choices = [category for category in category_choices if category[0] in allowed_categories]
    #
    #         # Convert back to a dictionary for use in the template
    #         category_choices = dict(allowed_categories)
    #
    #     else:
    #         # If the user is not a Client Admin User, use the original category choices
    #         category_choices = dict(CATEGORY_CHOICES)
    #     # Render the campaign form template with the retrieved data
    #         # Get user access permissions
    #     user_access = UserAccess.objects.filter(user=request.user).first()
    #     # Filter markets based on user's access permissions
    #     markets = product_models.Market.objects.all()
    #     if user_access:
    #         allowed_markets = user_access.allowed_markets.all()
    #         markets = markets.filter(market_name__in=allowed_markets)
    #     return render(
    #         request,
    #         "campaign_form.html",
    #         {
    #             "divisions": divisions,
    #             "local_brands": local_brands,
    #             "activities": activities,
    #             "product_objs": product_objs,
    #             "code_placement_choices": code_placement_choices,
    #             "utm_source_choices": utm_source_choices,
    #             "utm_medium_choices": utm_medium_choices,
    #             "category_choices": category_choices,
    #             # "category_choices": allowed_categories,
    #             "markets": markets,
    #         },
    #     )

    def get(self, request):
        """
        Handle GET request.

        Retrieves data needed for rendering the campaign form and returns a response.

        Args:
            request: HttpRequest object

        Returns:
            HttpResponse object
        """

        # Retrieve required data from models
        divisions = brand_models.Division.objects.filter()
        local_brands = brand_models.LocalBrand.objects.all().exclude(brand=None)
        activities = product_models.Activity.objects.all()
        code_placement_choices = dict(CODE_POSITION_CHOICES)
        utm_source_choices = dict(CODE_PLACEMENT_CHOICES)
        utm_medium_choices = dict(CODE_TYPE_CHOICES)
        product_objs = product_models.Product.objects.all()

        #fetching permissions from AccessTable for category and market
        user_permissions = AccessTable.objects.filter(user=request.user).first()
        if user_permissions:
            user_categories = user_permissions.category.all()
        else:
            user_categories = []

        # Filter category choices based on user's associated categories
        category_choices = brand_models.Category.objects.filter(id__in=user_categories)

        # Get user's allowed markets from AccessTable
        if user_permissions:
            allowed_markets = user_permissions.markets.all()
            markets = product_models.Market.objects.filter(market_name__in=allowed_markets)
        else:
            markets = []
        return render(
            request,
            "campaign_form.html",
            {
                "divisions": divisions,
                "local_brands": local_brands,
                "activities": activities,
                "product_objs": product_objs,
                "code_placement_choices": code_placement_choices,
                "utm_source_choices": utm_source_choices,
                "utm_medium_choices": utm_medium_choices,
                "category_choices": category_choices,
                "markets": markets,
            },
        )

    def post(self, request):
        """
        Handle POST request.

        Processes the submitted form data, saves the form if valid,
        and redirects the user accordingly.

        Args:
            request: HttpRequest object

        Returns:
            HttpResponse object
        """

        success = False
        error_message = None
        data = request.POST
        form = CampaignForm(data)

        # Validate the form data
        if form.is_valid():
            success, error_message, campaign_obj, campaign_detail_obj = form.save()
        else:
            error_message = form.errors.as_json()
            print(error_message)

        # Handle form submission outcome
        if success:
            campaign_obj.updated_by = request.user.username
            campaign_obj.save()
            messages.success(request, "Campaign form submitted successfully.")
            qr_request_form_url = (
                    reverse("qr_request_form")
                    + f"?campaign_id={campaign_obj.id}&market={data.get('market')}&launch_date={data.get('planned_launch_date')}"
            )
            return redirect(qr_request_form_url)
        else:
            messages.error(request, f"Failed to submit Campaign form - {error_message}")
            return redirect("/custom_admin_dashboard")


from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.models import Group


def group_users_list(request, group_id):
    group = Group.objects.get(pk=group_id)
    users = group.user_set.all()
    return render(request, 'group_users_list.html', {'group': group, 'users': users})
