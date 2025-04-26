from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .utils.email_verification import verify_email

app_name = 'users'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    
    # Password Reset URLs
    path('password-reset/', 
         auth_views.PasswordResetView.as_view(
             template_name='users/password_reset/password_reset.html',
             email_template_name='users/password_reset/password_reset_email.html',
             subject_template_name='users/password_reset/password_reset_subject.txt'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='users/password_reset/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='users/password_reset/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='users/password_reset/password_reset_complete.html'
         ),
         name='password_reset_complete'),
    
    # Email Verification URL
    path('verify-email/<uuid:token>/', verify_email, name='verify_email'),
]
