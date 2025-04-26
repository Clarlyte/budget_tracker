from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from ..models import User

def send_verification_email(user):
    """Send verification email to user"""
    subject = 'Verify your email address'
    html_message = render_to_string('users/email/verification_email.html', {
        'user': user,
        'verification_url': f"{settings.SITE_URL}/verify-email/{user.email_verification_token}/"
    })
    plain_message = strip_tags(html_message)
    
    send_mail(
        subject,
        plain_message,
        settings.DEFAULT_FROM_EMAIL,
        [user.email],
        html_message=html_message,
        fail_silently=False,
    )

def verify_email(request, token):
    """Verify user's email address"""
    try:
        user = User.objects.get(email_verification_token=token)
        user.is_email_verified = True
        user.email_verification_token = None
        user.save()
        messages.success(request, 'Your email has been verified successfully!')
    except User.DoesNotExist:
        messages.error(request, 'Invalid verification token.')
    
    return redirect('login') 