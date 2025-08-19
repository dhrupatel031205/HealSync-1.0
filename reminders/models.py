from django.db import models
from django.conf import settings
from medications.models import Medication


class Reminder(models.Model):
    medication = models.ForeignKey(Medication, on_delete=models.CASCADE, related_name='reminders')
    patient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reminders')
    reminder_time = models.DateTimeField()
    sent_status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Reminder for {self.medication} at {self.reminder_time}"
