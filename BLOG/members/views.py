from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.
def home(request):
    return render(request,'index.html')
def education(request):
    return render(request,'education.html')

def awards(request):
    return render(request,'awards.html')

def interest(request):
    return render(request,'interest.html')

def projects(request):
    return render(request,'projects.html')