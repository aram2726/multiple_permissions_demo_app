from django.contrib import admin

from .models import Polls


@admin.register(Polls)
class PollsAdmin(admin.ModelAdmin):
    pass
