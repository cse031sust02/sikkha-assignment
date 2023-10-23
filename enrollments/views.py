# enrollments/views.py
from rest_framework import generics
from .models import Enrollment
from .serializers import EnrollmentSerializer

class EnrollmentCreateView(generics.CreateAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
