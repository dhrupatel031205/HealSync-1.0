from rest_framework import serializers
from .models import MedicationLog


class MedicationLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicationLog
        fields = '__all__'
        read_only_fields = ['id', 'patient', 'created_at']
