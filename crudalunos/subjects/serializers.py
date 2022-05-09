"""" This will turn the Subject models into a JSON representation"""
from rest_framework import serializers
from .models import Subject


class SubjectSerializer(serializers.ModelSerializer):
    """ Serialize the subject data """

    class Meta:
        """ Serialize the subject data """
        model = Subject
        fields = '__all__'
