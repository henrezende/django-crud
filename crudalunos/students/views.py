""" Logic for a set of related views for the Student class """
from rest_framework import viewsets
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from crudalunos.common.utils import create_student_filter
from .models import Student
from .serializers import StudentCreateOrUpdateSerializer, StudentSerializer


class StudentViewSet(viewsets.ModelViewSet):  # pylint: disable=too-many-ancestors
    """ Students endpoints """
    queryset = Student.objects.all().order_by('id')

    def get_serializer_class(self):
        if self.action in ('create', 'update', 'partial_update'):
            return StudentCreateOrUpdateSerializer
        return StudentSerializer

    first_name = openapi.Parameter('first_name', openapi.IN_QUERY,
                                   description="example of a first name filter",
                                   type=openapi.TYPE_STRING)
    subjects = openapi.Parameter('subjects',
                                 in_=openapi.IN_QUERY,
                                 description='example of a subjects filter, must be a list of ids',
                                 type=openapi.TYPE_ARRAY,
                                 items=openapi.Items(
                                     type=openapi.TYPE_INTEGER)
                                 )
    response = openapi.Response(
        'response description', StudentSerializer)

    @swagger_auto_schema(manual_parameters=[first_name, subjects], responses={200: response})
    def list(self, request, *args, **kwargs):
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
