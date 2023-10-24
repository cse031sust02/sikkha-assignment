from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from .services import CourseService
from .serializers import CourseSerializer

class CourseListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = CourseSerializer

    def get_queryset(self):
        queryset = CourseService.get_courses()
        instructor = self.request.query_params.get('instructor', None)
        price = self.request.query_params.get('price', None)
        duration = self.request.query_params.get('duration', None)

        if instructor:
            queryset = queryset.filter(instructor__icontains=instructor)
        if price:
            queryset = queryset.filter(price=price)
        if duration:
            queryset = queryset.filter(duration=duration)

        return queryset

    def post(self, request, *args, **kwargs):
        # Implementation for creating a new course
        # Add your logic here
        return super().post(request, *args, **kwargs)


class CourseDetailAPIView(generics.RetrieveAPIView):
    queryset = CourseService.get_courses()
    serializer_class = CourseSerializer
