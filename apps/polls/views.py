from django.shortcuts import render
from django.views.generic import ListView, CreateView

from multiple_permissions.permissions import IsSuperuser, IsAuthenticated

from .forms import PollsForm
from .models import Polls


class PollsListView(ListView):
    form_class = PollsForm
    queryset = Polls.objects.all()
    permission_classes = IsAuthenticated,
    template_name = "polls/list_polls.html"

    def get(self, request, *args, **kwargs):
        data = self.queryset
        return render(request, self.template_name, {"data": data})


class PollsCreateView(CreateView):
    permission_classes = IsSuperuser,
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
