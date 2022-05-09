"""Configuration to show your models in admin interface"""
from django.contrib import admin
from .models import Subject

admin.site.register(Subject)
