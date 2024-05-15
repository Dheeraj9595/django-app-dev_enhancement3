from django.contrib.auth.models import Group
from django.contrib import admin
from django.contrib.auth.admin import GroupAdmin
from .models import Role
from django.contrib import admin
from django.contrib.auth.models import User
from RoleAccess.models import AccessTable
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# admin.site.unregister(Group)
from django.utils.translation import gettext_lazy as _

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from brands.models import BrandUserLink
from campaigns.models import CategoryUserLink


class AccessTables(admin.TabularInline):
    model = AccessTable
    extra = 0
    # template = 'access_permissions.html'


# class CustomUserModelAdmin(UserAdmin):
#     fieldsets = (
#         (None, {'fields': ('username', 'password')}),
#         ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
#         ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
#         ('Important dates', {'fields': ('last_login', 'date_joined')}),
#
#     )
#     inlines = [AccessTables]
#
#
# admin.site.unregister(User)
# admin.site.register(User, CustomUserModelAdmin)
#
#
@admin.register(Role)
class RoleAdmin(GroupAdmin):
    pass


#
#
# admin.site.unregister(User)
# admin.site.unregister(Group)
# admin.site.register(User, CustomUserModelAdmin)
# admin.site.register(AccessTable)

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.utils.translation import gettext_lazy as _


class AccessTables(admin.TabularInline):
    model = AccessTable
    extra = 0


"""Settigns for User's Tab"""


# Define a custom UserAdmin class
class CustomUserAdmin(UserAdmin):
    # Override the fieldsets to change the label for is_staff
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_active')

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('groups',), 'classes': ('collapse',)}),
        ('User Status', {'fields': ('is_active', 'is_superuser', 'is_staff'),
                         'description': "Designates whether the user is active."}),

    )
    inlines = [AccessTables]

    def formfield_for_manytomany(self, db_field, request=None, **kwargs):
        if db_field.name == 'groups':
            kwargs['label'] = 'Available roles'
            kwargs['help_text'] = 'Chosen roles'
            kwargs['widget'] = FilteredSelectMultiple('Roles', False)
        return super().formfield_for_manytomany(db_field, request, **kwargs)


# Unregister the default UserAdmin
admin.site.unregister(User)

# Register UserAdmin with the custom settings
admin.site.register(User, CustomUserAdmin)
admin.site.register(AccessTable)
