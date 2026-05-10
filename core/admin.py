from django.contrib import admin
from .models import UserProfile, AuditLog, Notification

# Register your models here.
admin.site.site_header = "Broadcast Engineering Teams Admin"
admin.site.site_title = "BET Admin"
admin.site.index_title = "Admin Dashboard"

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'role', 'department']

@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):
    list_display = ['user', 'action_type', 'table_name', 'timestamp', 'description']
    list_filter = ['action_type']
    readonly_fields = ['user', 'action_type', 'table_name', 'record_id', 'timestamp', 'description']

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ['user', 'message', 'read', 'created_at']

    