from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User

from .forms import LoginForm, RegisterForm


class RegisterView(View):
    """
    Register user view.
    """

    template_name = "users/register.html"
    form_class = RegisterForm

    def get(self, request):
        return render(request, self.template_name, {"form": self.form_class})

    def post(self, request):
        form = self.form_class(request.POST or None)
        if form.is_valid():
            user = form.save()
            return redirect("/users/login/")
        return render(request, self.template_name, {"form": form})


class LoginView(View):
    """
    Login user view.
    """

    template_name = "users/login.html"
    form_class = LoginForm

    def get(self, request):
        return render(request, self.template_name, {"form": self.form_class})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.authenticate(request)
            return redirect("/polls/list/")
        print(form.errors)
        return render(request, self.template_name, {"form": form})
