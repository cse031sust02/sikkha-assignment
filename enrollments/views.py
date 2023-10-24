from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .services import EnrollmentService

@api_view(['POST'])
def enroll_student(request):
    student_name = request.data.get('student_name')
    course_id = request.data.get('course_id')
    enrollment_date = request.data.get('enrollment_date')

    if not EnrollmentService.validate_enrollment(student_name, course_id):
        return Response({'detail': 'Sorry! Enrollment failed. The course does not exist'}, status=status.HTTP_400_BAD_REQUEST)

    enrollment = EnrollmentService.enroll_student(student_name, course_id, enrollment_date)
    return Response({'detail': 'Student enrolled successfully.'}, status=status.HTTP_201_CREATED)
