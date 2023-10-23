# courses/urls.py
from django.urls import path
from .views import CourseListCreateView, CourseRetrieveView

urlpatterns = [
    path('courses/', CourseListCreateView.as_view(), name='course-list-create'),
    path('courses/<int:pk>/', CourseRetrieveView.as_view(), name='course-detail'),
]
