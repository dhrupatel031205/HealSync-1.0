from django.contrib import admin
from .models import MedicationLog


@admin.register(MedicationLog)
class MedicationLogAdmin(admin.ModelAdmin):
    list_display = ('patient', 'medication', 'status', 'time_taken')
    list_filter = ('status',)
