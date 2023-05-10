from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


# Create your views here.
# def welcome(request):
# return HttpResponse("welcome amr")


def Resume(request):
    template = loader.get_template('show.html')
    return HttpResponse(template.render())
