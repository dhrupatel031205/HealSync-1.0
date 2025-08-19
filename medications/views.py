from rest_framework import viewsets, permissions
from .models import Medication
from .serializers import MedicationSerializer


class MedicationViewSet(viewsets.ModelViewSet):
    serializer_class = MedicationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'doctor':
            # Doctors can view medications of their assigned patients (simple demo: all)
            return Medication.objects.all()
        return Medication.objects.filter(patient=user)

    def perform_create(self, serializer):
        serializer.save(patient=self.request.user)
