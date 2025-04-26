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
        return self.cleaned_data.get('username') 