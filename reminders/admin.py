from django.contrib import admin
from .models import Reminder


@admin.register(Reminder)
class ReminderAdmin(admin.ModelAdmin):
    list_display = ('patient', 'medication', 'reminder_time', 'sent_status')
    list_filter = ('sent_status',)
