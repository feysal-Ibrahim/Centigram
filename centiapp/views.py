from django.shortcuts import render
from django.http import HttpResponse , Http404  # import the HttpResponse class from the django.http module.
from peewee import DoesNotExist
# Create your views here.

def home (request):
    return render(request,'index.html')