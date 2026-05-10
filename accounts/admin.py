from django.contrib import admin
from .models import PasswordResetToken

# Register your models here.
@admin.register(PasswordResetToken)
class PasswordResetTokenAdmin(admin.ModelAdmin):
    list_display = ['user', 'created_at', 'used']