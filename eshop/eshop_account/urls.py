from django.contrib.auth import logout
from django.urls import path
from .views import edit_user_profile, log_out, login_user,register, user_account_main_page



urlpatterns = [
    path('login', login_user),
    path('register', register),
    path('log-out', log_out),
    path('user',user_account_main_page),
    path('user/edit',edit_user_profile)
]
