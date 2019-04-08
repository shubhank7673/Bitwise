from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('home1',views.home1,name='home1'),

]
