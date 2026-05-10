from django.contrib import admin
<<<<<<< HEAD
from .models import Meetings
=======
from .models import Meeting
>>>>>>> 1bbd6c5 (Initial project setup)

# Register your models here.
@admin.register(Meeting)
class MeetingAdmin(admin.ModelAdmin):
    list_display = ['title', 'organiser', 'team', 'date_time', 'platform']