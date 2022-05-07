"""Configuration to show your models in admin interface"""
from django.contrib import admin
from .models import Student

admin.site.register(Student)