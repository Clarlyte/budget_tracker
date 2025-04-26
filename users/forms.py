from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import get_user_model, authenticate
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
        label=_('Username or Email'),
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

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            if '@' in username:
                try:
                    user = User.objects.get(email=username)
                    username = user.username
                except User.DoesNotExist:
                    pass

            self.user_cache = authenticate(
                self.request,
                username=username,
                password=password
            )
            if self.user_cache is None:
                raise forms.ValidationError(
                    _('Please enter a correct username/email and password.'),
                    code='invalid_login',
                )
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data