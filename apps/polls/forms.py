from django.forms import ModelForm

from .models import Polls


class PollsForm(ModelForm):
    class Meta:
        model = Polls
        fields = "__all__"
