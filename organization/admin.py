from django.contrib import admin
from .models import Department, TeamType

# Register your models here.

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['department_name', 'department_specialisation', 'department_head']
    search_fields = ['department_name']

@admin.register(TeamType)
class TeamTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']