from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("assingment no 1")

def home(request):
    return HttpResponse("<h1>pyspiders basvangudi</h1>")

def html_1(request):
    return render(request,"sample.html")