from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('auth/home', views.home, name='home'),
    path('signin', views.sign_in, name='signin'),
    path('signout', views.sign_out, name='signout'),
    path('callback', views.callback, name='callback'),

]
