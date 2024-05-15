from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import AccessMixin
from django.http import HttpResponseForbidden
from django.shortcuts import render


class AdminLoginRequiredMixin(LoginRequiredMixin):

    def dispatch(self, request, *args, **kwargs):
        """
        Check if the user is logged in and is a superuser
        """
        if not request.user.is_authenticated or not request.user.is_staff:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class GroupRequiredMixin(AccessMixin):
    """
    Mixin to restrict access based on user group membership.
    """
    required_groups = []

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()

        # Check if the user belongs to any of the required groups
        if not request.user.groups.filter(name__in=self.required_groups).exists():
            return render(request, "custom_admin_dashboard.html")

        return super().dispatch(request, *args, **kwargs)


class PermissionRequiredMixin(AccessMixin):
    """
    Mixin to restrict access based on user permissions.
    """
    required_permissions = []

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()

        # Check if the user has any of the required permissions
        if not request.user.has_perms(self.required_permissions):
            return render(request, '403_forbidden.html')

        return super().dispatch(request, *args, **kwargs)
