from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Meeting(models.Model):
    PLATFORM_CHOICES = [
        ('zoom', 'Zoom'),
        ('teams', 'Microsoft Teams'),
        ('google_meet', 'Google Meet'), 
        ('in_person', 'In Person'), 
        ('slack', 'Slack Huddle'),
    ]
    title = models.CharField(max_length=200)
    organiser = models.ForeignKey(User, on_delete=models.CASCADE, related_name='organised_meetings')
    team = models.ForeignKey('teams.Team', null=True, blank=True, on_delete=models.SET_NULL, related_name='meetings')
    attendees = models.ManyToManyField(User, related_name='meetings_attending', blank=True)
    date_time = models.DateTimeField()
    platform = models.CharField(max_length=20, choices=PLATFORM_CHOICES, default='zoom')
    meeting_link = models.URLField(blank=True)
    agenda = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.date_time.strftime('%d %b %Y %H:%M')}"
    
    class Meta:
        ordering = ['date_time']
    
