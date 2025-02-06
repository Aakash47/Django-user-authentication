from django.urls import path
from . import views as user_views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('', user_views.home, name='dashboard'),
    path('profile/', user_views.profile, name='profile'),
    path("register/", user_views.register, name="register"),
    path("login/", user_views.loginpage, name="login"),
    path("logout/", user_views.logoutuser, name="logout"),
    path("change-password/", user_views.change_password, name="change_password"),
    path('password-reset/', auth_view.PasswordResetView.as_view(template_name='password_reset.html'),name='password_reset'),
    path('password-reset/done/', auth_view.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset-complete/', auth_view.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name='password_reset_complete'),
]