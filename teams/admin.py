from django.contrib import admin
<<<<<<< HEAD

# Register your models here.
=======
from .models import Team, TeamMember, CodeRepository, ContactChannel, TeamDependency

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['team_name', 'department', 'manager', 'status', 'team_type']
    list_filter = ['status', 'department', 'team_type']
    search_fields = ['team_name', 'team_purpose']

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ['user', 'team', 'role_in_team']
    list_filter = ['team']

@admin.register(CodeRepository)
class CodeRepositoryAdmin(admin.ModelAdmin):
    list_display = ['repo_name', 'team', 'repo_uri']

@admin.register(ContactChannel)
class ContactChannelAdmin(admin.ModelAdmin):
    list_display = ['team', 'channel_type', 'contact_value']

@admin.register(TeamDependency)
class TeamDependencyAdmin(admin.ModelAdmin):
    list_display = ['team', 'depends_on', 'dependency_type']
>>>>>>> 1bbd6c5 (Initial project setup)
