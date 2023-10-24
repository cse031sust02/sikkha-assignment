from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .services import EnrollmentService
from .serializers import EnrollmentSerializer

class EnrollmentListCreateAPIView(generics.ListCreateAPIView):
    queryset = EnrollmentService.get_enrollments()
    serializer_class = EnrollmentSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Validate enrollment before creating
        student_name = serializer.validated_data.get('student_name', '')
        course = serializer.validated_data.get('course', '')
        if not EnrollmentService.validate_enrollment(student_name, course):
            return Response({"error": "The course does not exist"}, status=status.HTTP_400_BAD_REQUEST)

        EnrollmentService.enroll_student(student_name, course, serializer.validated_data.get('enrollment_date', ''))
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
