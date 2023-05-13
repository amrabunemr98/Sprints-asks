from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Student
from .models import Course


# Create your views here.
# def welcome(request):
# return HttpResponse("welcome amr")


def Resume(request):
    template = loader.get_template('show.html')
    return HttpResponse(template.render())


def student_view(request):
    context = {}
    context["dataset"] = Student.objects.all()
    return render(request, "student_view.html", context)


def courses_view(request):
    context = {}
    context["dataset"] = Course.objects.all()
    return render(request, "course_view.html", context)