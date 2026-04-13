from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('home page')

def students(request):
    return HttpResponse('students page')

def about(request):
    return render(request, 'about.html')