from django import forms
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from apps.core.forms import BootstrapForm


class LoginForm(BootstrapForm):
    """
    Login form.
    """

    username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get("username")
        raw_password = self.cleaned_data.get("password")
        try:
            user = User.objects.get(username=username)
        except User.DoesnotExist:
            raise ValidationError("Invalid credentials.")
        if user.check_password(raw_password):
            self.cleaned_data["user"] = user
        else:
            raise ValidationError("Invalid credentials.")

    def authenticate(self, request):
        login(request, self.cleaned_data["user"])


class RegisterForm(UserCreationForm, BootstrapForm):
    """
    Create a new user.
    """
