from django.db import models
from django.conf import settings


class Medication(models.Model):
    class Form(models.TextChoices):
        PILL = 'pill', 'Pill'
        LIQUID = 'liquid', 'Liquid'
        INJECTION = 'injection', 'Injection'

    name = models.CharField(max_length=255)
    dosage = models.CharField(max_length=100)
    form = models.CharField(max_length=50, choices=Form.choices)
    frequency = models.CharField(max_length=100)
    instructions = models.TextField(blank=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    patient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='medications')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.name} - {self.patient}"
