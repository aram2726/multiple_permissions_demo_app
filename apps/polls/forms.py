from django.forms import ModelForm

from apps.core.forms import BootstrapForm
from .models import Polls


class PollsForm(ModelForm, BootstrapForm):
    class Meta:
        model = Polls
        fields = "__all__"
