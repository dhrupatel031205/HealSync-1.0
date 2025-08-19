from django.contrib import admin
from .models import Medication


@admin.register(Medication)
class MedicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'patient', 'form', 'frequency', 'start_date', 'end_date')
    search_fields = ('name', 'patient__username')
