from django.contrib import admin
from .models import kodeathon

@admin.register(kodeathon)
class kodeathonA(admin.ModelAdmin):
    pass

