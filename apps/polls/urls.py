from django.urls import path

from .views import PollsListView, PollsCreateView

urlpatterns = [
    path("", PollsListView.as_view()),
    path("polls-create", PollsCreateView.as_view()),
]
