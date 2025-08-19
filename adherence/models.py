from django.db import models
from django.conf import settings
from medications.models import Medication


class MedicationLog(models.Model):
    class Status(models.TextChoices):
        TAKEN = 'taken', 'Taken'
        SKIPPED = 'skipped', 'Skipped'
        DELAYED = 'delayed', 'Delayed'

    medication = models.ForeignKey(Medication, on_delete=models.CASCADE, related_name='logs')
    patient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='medication_logs')
    time_taken = models.DateTimeField()
    status = models.CharField(max_length=20, choices=Status.choices)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.patient} - {self.medication} - {self.status}"
