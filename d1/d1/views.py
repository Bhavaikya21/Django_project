from django.http import HttpResponse
def index(request):
    return HttpResponse("Hello Bhavaikya")

def home(request):
    return HttpResponse("<h1>Welcome Bhavaikya<h1>")