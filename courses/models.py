# courses/models.py
from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    instructor = models.CharField(max_length=100)
    duration = models.IntegerField()
    price = models.FloatField()

    def __str__(self):
        return self.title
