import operator
from functools import reduce
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
# from drf_yasg.utils import swagger_auto_schema
# from drf_yasg import openapi
from django.db.models import Q
from .models import Student
from .serializers import StudentSerializer

class StudentViewSet(viewsets.ModelViewSet):
    """" Students endpoints """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def list(self, request):
        serializer_context = {
            'request': request,
        }

        list_of_Q = Q()
        simple_condition = ""
        for key in request.GET:
            valuelist = request.GET.getlist(key)
            simple_condition = reduce(operator.or_, (Q(**{key: val})
                for val in valuelist))
            list_of_Q.add(simple_condition, Q.AND)

        result = Student.objects.filter(list_of_Q)

        page = self.paginate_queryset(result)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = StudentSerializer(result, many=True, context=serializer_context)
        return Response(serializer.data)
