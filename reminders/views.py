from rest_framework import generics, permissions
from .models import Reminder
from .serializers import ReminderSerializer


class ReminderListView(generics.ListAPIView):
    serializer_class = ReminderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Reminder.objects.filter(patient=self.request.user)
