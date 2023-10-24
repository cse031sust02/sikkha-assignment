from .models import Enrollment
from courses.models import Course
from django.http import Http404

class EnrollmentService:
    @staticmethod
    def enroll_student(student_name, course, enrollment_date):
        return Enrollment.objects.create(student_name=student_name, course=course, enrollment_date=enrollment_date)

    @staticmethod
    def get_enrollments():
        return Enrollment.objects.all()
    
    @staticmethod
    def validate_enrollment(student_name, course):
        # TODO : I am not fully sure on business requirements for validation
        try:
            if student_name and course:
                return True
            else:
                return False
        except Course.DoesNotExist:
            raise Http404("The course does not exist")
