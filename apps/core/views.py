from django.shortcuts import render
from django.views import View


class HomePageView(View):
    """
    Home page.
    """

    def get(self, request):
        return render(request, "home.html", {})
