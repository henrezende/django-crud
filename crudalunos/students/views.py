import operator
from functools import reduce
from django.shortcuts import render
from crudalunos.common.utils import create_student_filter
from crudalunos.subjects.models import Subject
from rest_framework import viewsets, status
from rest_framework.response import Response
# from drf_yasg.utils import swagger_auto_schema
# from drf_yasg import openapi
from django.db.models import Q
from .models import Student
from .serializers import StudentCreateSerializer, StudentSerializer


class StudentViewSet(viewsets.ModelViewSet):
    """" Students endpoints """
    queryset = Student.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return StudentCreateSerializer
        return StudentSerializer

    def list(self, request):
        serializer_context = {
            'request': request,
        }

        query_list = create_student_filter(request)
        result = Student.objects.filter(query_list)

        page = self.paginate_queryset(result)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = StudentSerializer(
            result, many=True, context=serializer_context)
        return Response(serializer.data)
