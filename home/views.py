from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'home3.html')
def home1(request):
    return render(request,'home.html')
def developers(request):
    return HttpResponse("<h1>Shubhank Khare</h1><h1>Piyush Jain</h1>The site is in development phase")
def about(request):
    return render(request,'about.html')
def error_404_view(request, exception):
    return render(request,'Error.html')
