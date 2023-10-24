from django.urls import path
from .views import EnrollmentListCreateAPIView

urlpatterns = [
    path('enrollments', EnrollmentListCreateAPIView.as_view(), name='enrollment-list-create'),
]
