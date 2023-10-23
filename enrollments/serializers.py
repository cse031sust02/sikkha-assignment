# enrollments/serializers.py
from rest_framework import serializers
from courses.models import Course
from .models import Enrollment

class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = '__all__'
