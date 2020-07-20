from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("<marquee>Hello Bhavaikya<marquee>")

def html1(request):
    return render(request, "sample1.html")