from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first(request):
    return HttpResponse('This is first view')
def second(request):
    return HttpResponse('<h1> welcome to django framework </h1>')