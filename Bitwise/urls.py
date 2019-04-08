from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls'),name="Home"),
    path('',include('kodeathon.urls'),name="Kodeathon"),
    path('',include('events.urls'),name="Events"),
    path('',include('team.urls'),name="Team"),
]
