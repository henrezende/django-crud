import operator
from functools import reduce
from django.shortcuts import render
from crudalunos.common.utils import create_student_filter
from crudalunos.subjects.models import Subject
from rest_framework import viewsets, status
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
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

    first_name = openapi.Parameter('first_name', openapi.IN_QUERY,
                                   description="example of a first name filter", type=openapi.TYPE_STRING)
    subjects = openapi.Parameter('subjects',
                                 in_=openapi.IN_QUERY,
                                 description='example of a subjects filter, that must be a list of ids',
                                 type=openapi.TYPE_ARRAY,
                                 items=openapi.Items(
                                     type=openapi.TYPE_INTEGER)
                                 )
    student_response = openapi.Response(
        'response description', StudentSerializer)

    @swagger_auto_schema(manual_parameters=[first_name, subjects, ], responses={200: student_response})
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
