from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

User = get_user_model()

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(
        label=_('Email'),
        max_length=254,
        widget=forms.EmailInput(attrs={'autocomplete': 'email'})
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        label=_('Email'),
        widget=forms.TextInput(attrs={'autofocus': True})
    )
    
    def clean_username(self):
        username_or_email = self.cleaned_data.get('username')
        if '@' in username_or_email:  # Check if input looks like an email address
            try:
                user = User.objects.get(email=username_or_email)
                return user.username
            except User.DoesNotExist:
                raise forms.ValidationError(
                    _('No user is associated with this email address.'),
                    code='invalid_login',
                )
        return username_or_email  # Return as is if not an email