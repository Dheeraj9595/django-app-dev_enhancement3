from django.contrib import admin
from .models import Brand, Division, LocalBrand
from django.contrib import admin
from .models import BrandUserLink

from django.contrib import admin
from .models import Brand
from .forms import BrandForm


class BrandAdmin(admin.ModelAdmin):
    form = BrandForm


admin.site.register(Brand, BrandAdmin)


class BrandUserLinkAdmin(admin.ModelAdmin):
    list_display = ('user', 'display_local_brands')

    def display_local_brands(self, obj):
        return ", ".join([str(brand) for brand in obj.local_brands.all()])

    display_local_brands.short_description = 'Local Brands'


admin.site.register(BrandUserLink, BrandUserLinkAdmin)
# admin.site.register(Brand)
admin.site.register(Division)
admin.site.register(LocalBrand)

# from django.contrib import admin
# from django.contrib.auth.models import Group
# from django.utils.translation import gettext_lazy as _
#
#
# class GroupAdmin(admin.ModelAdmin):
#     list_display = ['name', 'user_count', 'user_info']
#
#     def user_count(self, obj):
#         return obj.user_set.count()
#
#     user_count.short_description = _('User count')
#
#     def user_info(self, obj):
#         users = obj.user_set.all()
#         return '\n'.join([f"({user.email})" for user in users])
#
#     user_info.short_description = _('Users')
#
#
# # Unregister the default GroupAdmin
# admin.site.unregister(Group)
#
# # Register GroupAdmin with the custom settings
# admin.site.register(Group, GroupAdmin)
