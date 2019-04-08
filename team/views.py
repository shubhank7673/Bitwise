from django.shortcuts import render
from django.http import HttpResponse

def team(request):
    return render(request,"team.html")
