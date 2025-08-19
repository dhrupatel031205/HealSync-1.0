from rest_framework import generics, permissions
from .models import MedicationLog
from .serializers import MedicationLogSerializer


class MedicationLogListCreateView(generics.ListCreateAPIView):
    serializer_class = MedicationLogSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return MedicationLog.objects.filter(patient=self.request.user).select_related('medication')

    def perform_create(self, serializer):
        serializer.save(patient=self.request.user)
