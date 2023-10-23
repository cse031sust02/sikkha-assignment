# enrollments/models.py
from django.db import models
from courses.models import Course

class Enrollment(models.Model):
    student_name = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrollment_date = models.DateField()

    def __str__(self):
        return f"{self.student_name} - {self.course.title}"
