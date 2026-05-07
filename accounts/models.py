from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class PasswordResetToken(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    token = models.CharField(max_length = 100, unique = True)
    created_at = models.DateTimeField(auto_now_add = True)
    used = models.BooleanField(default = False)

    def __str__(self):
        return f"Reset token for {self.user.username}"