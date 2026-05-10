from django.db import models
from django.contrib.auth.models import User
from organization.models import Department, TeamType


class Team(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('disbanded', 'Disbanded'),
        ('restructuring', 'Restructuring'),
    ]
    team_name = models.CharField(max_length=100)
    team_purpose = models.TextField(blank=True)
    team_contactemail = models.EmailField(blank=True)
    manager = models.ForeignKey(
        User, null=True, blank=True,
        on_delete=models.SET_NULL, related_name='managed_teams'
    )
    department = models.ForeignKey(
        Department, null=True, blank=True,
        on_delete=models.SET_NULL, related_name='teams'
    )
    team_type = models.ForeignKey(
        TeamType, null=True, blank=True,
        on_delete=models.SET_NULL, related_name='teams'
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.team_name


class TeamMember(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='members')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='team_memberships')
    role_in_team = models.CharField(max_length=100, blank=True)
    skills = models.TextField(blank=True)

    class Meta:
        unique_together = ('team', 'user')

    def __str__(self):
        return f"{self.user.get_full_name()} in {self.team.team_name}"


class CodeRepository(models.Model):
    repo_name = models.CharField(max_length=100)
    repo_uri = models.URLField(blank=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='repositories')

    def __str__(self):
        return self.repo_name


class ContactChannel(models.Model):
    CHANNEL_TYPES = [
        ('email', 'Email'),
        ('slack', 'Slack'),
        ('teams', 'Microsoft Teams'),
        ('phone', 'Phone'),
        ('other', 'Other'),
    ]
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='contact_channels')
    channel_type = models.CharField(max_length=20, choices=CHANNEL_TYPES)
    contact_value = models.CharField(max_length=200)
    contact_desc = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.channel_type}: {self.contact_value}"


class TeamDependency(models.Model):
    DEPENDENCY_TYPES = [
        ('upstream', 'Upstream'),
        ('downstream', 'Downstream'),
    ]
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='dependencies')
    depends_on = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='dependents')
    dependency_type = models.CharField(max_length=20, choices=DEPENDENCY_TYPES)
    description = models.TextField(blank=True)

    class Meta:
        unique_together = ('team', 'depends_on')

    def __str__(self):
        return f"{self.team} → {self.depends_on} ({self.dependency_type})"
