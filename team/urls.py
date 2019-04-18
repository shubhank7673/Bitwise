from django.urls import path,include
from . import views

urlpatterns = [
    path('team/',views.team,name='team'),
    path('testteam/',views.testteam,name='testteam')
]
