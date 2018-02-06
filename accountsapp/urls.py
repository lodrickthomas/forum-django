from django.urls import path
from . import views
from django.contrib.auth.views import (
    login,logout,password_reset,password_reset_done,
    password_reset_confirm,password_reset_complete,  )
    # password_change,password_change_done,


urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('login/', login, {'template_name': 'accountsapp/login.html'},  name='login'),
    path('logout/', logout, {'template_name': 'accountsapp/logout.html'},  name='logout'),
    path('registration/', views.registration, name='registration'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit', views.edit_profile, name='edit_profile'),
    path('change-password/', views.change_password, name='change_password'),
    path('reset-password/', password_reset, {'template_name': 'accountsapp/reset_password.html'},  name='reset_password'),
    path('reset-password/done/', password_reset_done, name='password_reset_done'),
    path('reset-password/confirm/(<uidb64>[0-9A-Za-z]+)-(<token>.+)/', password_reset_confirm, name='password_reset_confirm'),
    path('reset-password/complete/', password_reset_complete, name='password_reset_complete'),
    
]