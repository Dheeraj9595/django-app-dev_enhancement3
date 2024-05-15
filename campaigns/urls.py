from django.urls import path

from .views import CampaignFormView, group_users_list

urlpatterns = [
    path("campaign_form/", CampaignFormView.as_view(), name="campaign_form"),
    path('admin/group_users_list/<int:group_id>/', group_users_list, name='group_users_list'),
]
