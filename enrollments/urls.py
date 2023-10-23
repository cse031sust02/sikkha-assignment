# enrollments/urls.py
from django.urls import path
from .views import EnrollmentCreateView

urlpatterns = [
    path('enrollments/', EnrollmentCreateView.as_view(), name='enrollment-create'),
]
