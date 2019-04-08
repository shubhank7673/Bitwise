from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'homenew.html')
def home1(request):
    return render(request,'home.html')
