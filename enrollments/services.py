# enrollments/services.py
from .models import Enrollment
from courses.models import Course

class EnrollmentService:
    @staticmethod
    def enroll_student(student_name, course_id, enrollment_date):
        return Enrollment.objects.create(student_name=student_name, course_id=course_id, enrollment_date=enrollment_date)

    @staticmethod
    def validate_enrollment(student_name, course_id):
        try:
            course = Course.objects.get(id=course_id)
            # Additional validation logic can be added here
            if student_name and course:
                return True
            else:
                return False
        except Course.DoesNotExist:
            return False
