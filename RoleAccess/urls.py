from django.urls import path
from .views import AssignGroupView, RemoveUserFromRoleView, toggle_user_status,  user_detail

urlpatterns = [path('assign_group/', AssignGroupView.as_view(), name='assign_group'),
               path('remove-user-from-role/', RemoveUserFromRoleView.as_view(), name='remove_user_from_role'),
               path('status/', toggle_user_status, name='toggle_user_status'),
               path('user_detail/<int:user_id>/', user_detail, name='user_detail'),
               ]
