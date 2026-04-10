from django.contrib import admin
from .models import Meeting
@admin.register(Meeting)
class MeetingAdmin(admin.ModelAdmin):
    list_display = ['title', 'organiser', 'team', 'date_time', 'platform']
