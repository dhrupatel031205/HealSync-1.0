from django.db import models
from django.conf import settings


class EmergencyContact(models.Model):
    patient = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='emergency_contact')
    name = models.CharField(max_length=255)
    relation = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)

    def __str__(self) -> str:
        return f"{self.name} ({self.relation}) for {self.patient}"


class Notification(models.Model):
    class Type(models.TextChoices):
        EMAIL = 'email', 'Email'
        SMS = 'sms', 'SMS'
        PUSH = 'push', 'Push'

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='notifications')
    type = models.CharField(max_length=10, choices=Type.choices)
    message = models.TextField()
    status = models.CharField(max_length=20, default='pending')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.type} to {self.user} - {self.status}"
