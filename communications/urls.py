from django.urls import path
from .views import EmergencyContactView, NotificationCreateView


urlpatterns = [
    path('emergency-contact/', EmergencyContactView.as_view(), name='emergency-contact'),
    path('notifications/', NotificationCreateView.as_view(), name='notification-create'),
]
