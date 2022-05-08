from crudalunos.subjects.serializers import SubjectSerializer
from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):

    subjects = SubjectSerializer(many=True)

    class Meta:
        model = Student
        fields = '__all__'
        depth = 1


class StudentCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = '__all__'
