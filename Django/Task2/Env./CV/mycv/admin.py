from django.contrib import admin
from .models import Student
from .models import Course


class StudentAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name",)


class CourseAdmin(admin.ModelAdmin):
    list_display = ("course_name",)


admin.site.register(Student, StudentAdmin)
admin.site.register(Course, CourseAdmin)