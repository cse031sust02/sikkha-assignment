from django.test import TestCase
from .services import CourseService

class CourseServiceTestCase(TestCase):
    def test_get_courses(self):
        # Test the get_courses method
        courses = CourseService.get_courses()
        self.assertEqual(len(courses), 0)  # Assuming no courses are initially present

    def test_create_course(self):
        # Test the create_course method
        course = CourseService.create_course('Test Course', 'Test Description', 'Test Instructor', 60, 29.99)
        self.assertEqual(course.title, 'Test Course')
        self.assertEqual(course.description, 'Test Description')
        self.assertEqual(course.instructor, 'Test Instructor')
        self.assertEqual(course.duration, 60)
        self.assertEqual(course.price, 29.99)

    def test_filter_courses(self):
        # Test the filter_courses method
        filtered_courses = CourseService.filter_courses(instructor='Test Instructor', price=29.99, duration=60)
        self.assertIsNotNone(filtered_courses)
