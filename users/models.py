from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    """Custom User model that extends Django's AbstractUser"""
    email = models.EmailField(_('email address'), unique=True)
    
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.email
