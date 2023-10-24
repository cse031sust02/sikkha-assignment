from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from .services import CourseService
from .serializers import CourseSerializer


class CourseListCreateAPIView(APIView):
    def get(self, request, format=None):
        courses = CourseService.get_courses()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            title = serializer.validated_data['title']
            description = serializer.validated_data['description']
            instructor = serializer.validated_data['instructor']
            duration = serializer.validated_data['duration']
            price = serializer.validated_data['price']

            course = CourseService.create_course(
                title, description, instructor, duration, price)

            response_serializer = CourseSerializer(course)
            return Response(response_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CourseDetailAPIView(generics.RetrieveAPIView):
    queryset = CourseService.get_courses()
    serializer_class = CourseSerializer
