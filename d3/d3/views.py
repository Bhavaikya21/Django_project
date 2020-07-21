from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("<marquee>Hello Bhavaikya<marquee>")

def html1(request):
    return render(request, "sample1.html")

def html2(request):
    fruits =['banana', 'apple', 'grapes', 'mango']
    return render(request, "sample2.html", context = {'data' : 'Bhavaikya', 'name' : 'Chirag', 'fruits' : i})

def html3(request):
    return render (request,"sample3.html",{'a':5,'b':8})