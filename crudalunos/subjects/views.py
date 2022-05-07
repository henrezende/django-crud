import operator
from functools import reduce
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
# from drf_yasg.utils import swagger_auto_schema
# from drf_yasg import openapi
from django.db.models import Q
from .models import Subject
from .serializers import SubjectSerializer

class SubjectViewSet(viewsets.ModelViewSet):
    """" Subjects endpoints """
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
