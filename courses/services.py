# courses/services.py
from .models import Course

class CourseService:
    @staticmethod
    def get_courses():
        return Course.objects.all()

    @staticmethod
    def create_course(title, description, instructor, duration, price):
        return Course.objects.create(title=title, description=description, instructor=instructor, duration=duration, price=price)

    @staticmethod
    def get_course_by_id(course_id):
        return Course.objects.get(pk=course_id)

    @staticmethod
    def filter_courses(instructor=None, price=None, duration=None):
        courses = Course.objects.all()
        if instructor:
            courses = courses.filter(instructor__icontains=instructor)
        if price:
            courses = courses.filter(price=price)
        if duration:
            courses = courses.filter(duration=duration)
        return courses
