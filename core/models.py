from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, related_name = 'profile')
    department = models.ForeignKey(
        'organization.Department', null = True, blank = True, on_delete = models.SET_NULL
    )
    role = models.CharField(max_length = 100, blank = True)
    bio = models.TextField(blank = True)

    def __str__(self):
        return f"Profile of {self.user.username}"

class AuditLog(models.Model):
    user = models.ForeignKey(User, null = True, on_delete = models.SET_NULL)
    action_type = models.CharField(max_length = 20)
    table_name = models.CharField(max_length=100)
    record_id = models.IntegerField(null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ['-timestamp']
    
    def __str__(self):
        return f"{self.action_type} on {self.table_name} at {self.timestamp}"
    
class Notification(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'notifications')
    message = models.CharField(max_length=255)
    link = models.CharField(max_length=200, blank=True)
    read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Notification for {self.user.username} : {self.message}"