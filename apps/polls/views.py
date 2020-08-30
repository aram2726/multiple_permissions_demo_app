from django.shortcuts import render
from django.views.generic import ListView, CreateView

from multiple_permissions.permissions import IsSuperuser, IsAuthenticated

from .forms import PollsForm
from .models import Polls, ANSWER_CHOICES


class PollsListView(ListView):
    form_class = PollsForm
    queryset = Polls.objects.all()
    multiple_permissions = IsAuthenticated,
    template_name = "polls/list_polls.html"

    def get(self, request, *args, **kwargs):
        data = self.queryset
        answers = ANSWER_CHOICES
        return render(request, self.template_name, {"data": data, "answers": answers})


class PollsCreateView(CreateView):
    multiple_permissions = IsSuperuser,
    form_class = PollsForm
    queryset = Polls.objects.all()
    template_name = "polls/create_polls.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {"form": self.form_class})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return render(request, self.template_name, {"form": self.form_class})
        return render(request, self.template_name, {"form": self.form_class, "message": str(form.errors)})
