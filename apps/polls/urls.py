from django.urls import path

from .views import PollsListView, PollsCreateView

urlpatterns = [
    path("list/", PollsListView.as_view(), name="polls_create"),
    path("create/", PollsCreateView.as_view(), name="polls_create"),
]
