from django.urls import path
from . import views

urlpatterns = [
    path('kodeathon/',views.kodeathon,name='kodeathon'),
]
