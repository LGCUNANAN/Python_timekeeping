from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser, BaseUserManager



class TimeRecord(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    time_in = models.DateTimeField(null=True, blank=True)
    time_out = models.DateTimeField(null=True, blank=True)
    total_time = models.DurationField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.time_out and self.time_in:
            self.total_time = self.time_out - self.time_in
        super().save(*args, **kwargs)
    def total_time_display(self):
        if self.time_out and self.time_in:
            duration = self.time_out - self.time_in
            hours, minutes, seconds = duration.seconds // 3600, (duration.seconds // 60) % 60, duration.seconds % 60
            return f"{hours} hours, {minutes} minutes"
        return ""
    total_time_display.short_description = 'Total time'
    
class UserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('The username field must be set')
        username = self.normalize_username(username)
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, password, **extra_fields)
    
    def normalize_username(self, username):
        return username.strip().lower()


class User(AbstractUser):
    username = models.CharField(max_length=255,unique=True)
    is_employee = models.BooleanField("Is Employee", default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = UserManager()
