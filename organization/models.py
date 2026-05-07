from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Department(models.Model):
    department_name = models.CharField(max_length=100)
    department_specialisation = models.TextField(blank=True)
    department_head = models.ForeignKey(
        User, null=True, blank=True, 
        on_delete=models.SET_NULL, related_name='headed_departments'
    )

    def __str__(self):
        return self.department_name
    
    def team_count(self):
        return self.teams.count()
    
class TeamType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
