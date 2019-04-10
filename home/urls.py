from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('testhome',views.home1,name='home1'),
    path('developers',views.developers,name='developers'),
    path('about',views.about,name='about')

]
