from django.test import TestCase
from .services import EnrollmentService

class EnrollmentServiceTestCase(TestCase):
    def test_enroll_student(self):
        # Test the enroll_student method
        enrollment = EnrollmentService.enroll_student('John Doe', 1, '2023-10-01')
        self.assertIsNotNone(enrollment)

    def test_validate_enrollment_invalid(self):
        # Test the validate_enrollment method for an invalid case
        is_valid = EnrollmentService.validate_enrollment('', 1)
        self.assertFalse(is_valid)
