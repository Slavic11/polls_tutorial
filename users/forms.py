from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField, AuthenticationForm

User = get_user_model()


class UserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User


class UserLoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput, max_length=30)
    password = forms.CharField(widget=forms.PasswordInput, max_length=20)
