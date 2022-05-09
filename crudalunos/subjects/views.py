""" Logic for a set of related views for the Subject class """
from rest_framework import viewsets
from .models import Subject
from .serializers import SubjectSerializer


class SubjectViewSet(viewsets.ModelViewSet):  # pylint: disable=too-many-ancestors
    """" Subjects endpoints """
    queryset = Subject.objects.all().order_by('id')
    serializer_class = SubjectSerializer
