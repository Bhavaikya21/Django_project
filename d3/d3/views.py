from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("<marquee>Hello Bhavaikya<marquee>")

def html1(request):
    return render(request, "sample1.html")

def html2(request):
    fruits =['banana', 'apple', 'grapes', 'mango']
    return render(request, "sample2.html", context = {'data' : 'Bhavaikya', 'name' : 'Chirag', 'fruits' : fruits})

def html3(request):
    return render (request,"sample3.html",{'a':5,'b':8})

def urls_data(request,name):
    return HttpResponse('<h1>{}</h1>'.format(name))

def ab(request,ab):
    a=ab.split(" ")
    sum = int(a[0]) + int(a[1])
    return HttpResponse(str(sum))

def grt(request,grt):
    b = grt.split(" ")
    if int(b[0]) > int(b[1]):
        return HttpResponse(str(b[0]))
    else:
        return HttpResponse(str(b[1]))

def vow(request,s):
    m = 'aeiouAEIOU'
    v = 0
    c = 0
    for j in s:
        if j in m:
            v+=1
        else:
            c+=1
    return render(request,"vowels.html", context={'t':v, 'p':c})
    
    