from .models import Student
from .models import Course
from django.contrib import admin


# class StudentAdmin(admin.ModelAdmin):
    # list_display = ("first_name", "last_name",)


# class CourseAdmin(admin.ModelAdmin):
   # list_display = ("course_name",)


admin.site.register(Student)
admin.site.register(Course)

