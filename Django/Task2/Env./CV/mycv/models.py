from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)


class Course(models.Model):
    course_name = models.CharField(max_length=255)
