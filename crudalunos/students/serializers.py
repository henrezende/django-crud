"""" This will turn the Student models into a JSON representation"""
from rest_framework import serializers
from crudalunos.subjects.serializers import SubjectSerializer
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    """ Serialize the student data for get methods """
    subjects = SubjectSerializer(many=True)

    class Meta:
        """ Serialize the student data for get methods """
        model = Student
        fields = '__all__'
        depth = 1


class StudentCreateSerializer(serializers.ModelSerializer):
    """ Serialize the student data for creation method """
    class Meta:
        """ Serialize the student data for creation method """
        model = Student
        fields = '__all__'
