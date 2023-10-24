from django.urls import path
from . import views

urlpatterns = [
    path('enrollments/', views.enroll_student, name='enroll_student'),
]
