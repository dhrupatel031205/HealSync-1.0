from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import EmergencyContact, Notification
from .serializers import EmergencyContactSerializer, NotificationSerializer


class EmergencyContactView(generics.RetrieveUpdateAPIView):
    serializer_class = EmergencyContactSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        contact, _ = EmergencyContact.objects.get_or_create(patient=self.request.user)
        return contact


class NotificationCreateView(generics.CreateAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]
