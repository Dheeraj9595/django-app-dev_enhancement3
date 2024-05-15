from django.contrib import admin

from .models import Campaign, CampaignAdditionalDetails, CategoryUserLink


# from campaigns.forms import CampaignAdditionalDetailsForm


# class CampaignAdmin(admin.ModelAdmin):
#     search_fields = ("campaign_name",)
class CampaignAdmin(admin.ModelAdmin):
    list_display = (
        'campaign_name', 'key_contact_first_name', 'key_contact_last_name', 'date_added', 'date_updated')
    history_list_display = ["__str__", "date_updated"]
    ordering = ['-date_added']  # Default ordering by date_added, you can change this as needed
    list_filter = ('campaign_name',)

    def history_view(self, request, object_id, extra_context=None):
        extra_context = extra_context or {}
        obj = self.get_object(request, object_id)
        history = obj.history.all()
        extra_context['history'] = history
        return super().history_view(request, object_id, extra_context)

    def get_ordering(self, request):
        """
        Returns the ordering tuple for the queryset.

        This method allows you to dynamically change the ordering based on user input.
        """
        ordering = super().get_ordering(request)
        sort_by = request.GET.get('sort_by')
        if sort_by == 'alphabetical':
            return ('campaign_name',)
        elif sort_by == 'created_date':
            return ('-date_added',)
        elif sort_by == 'last_edited_date':
            return ('-date_updated',)
        else:
            return ordering


class UserAccessCategory(admin.ModelAdmin):
    list_display = ('user',)


class CampaignAdditionalDetailsAdmin(admin.ModelAdmin):
    search_fields = ("campaign__campaign_name",)
    list_filter = ('division', 'category')


from django.urls import reverse
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _


class GroupAdmin(admin.ModelAdmin):
    list_display = ['name', 'user_count', 'user_info']

    def user_count(self, obj):
        return obj.user_set.count()

    user_count.short_description = _('User count')

    def user_info(self, obj):
        users = obj.user_set.all()
        user_count = users.count()
        user_list = users[:5]  # Display only the first 5 users by default
        more_users_link = ''
        if user_count > 5:
            more_users_link = format_html('<br/><a href="{}" class="button">View all {} users</a>',
                                          reverse('admin:group_users_list', args=[obj.id]),
                                          user_count)
        users_info = '<br/>'.join([f"({user.email})" for user in user_list])
        return format_html(f'{users_info}{more_users_link}')

    user_info.short_description = _('Users')


admin.site.register(Campaign, CampaignAdmin)
admin.site.register(CampaignAdditionalDetails, CampaignAdditionalDetailsAdmin)
admin.site.register(CategoryUserLink, UserAccessCategory)
