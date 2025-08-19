from django.urls import path
from .views import MedicationLogListCreateView


urlpatterns = [
    path('', MedicationLogListCreateView.as_view(), name='log-list-create'),
]
