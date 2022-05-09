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


class StudentCreateOrUpdateSerializer(serializers.ModelSerializer):
    """ Serialize the student data for create and update methods """
    class Meta:
        """ Serialize the student data for create and update methods """
        model = Student
        fields = '__all__'

    def update(self, instance, validated_data):
        """ Override update method to handle nested subjects """
        subjects = validated_data.pop('subjects', [])
        instance = super().update(instance, validated_data)
        for subject in subjects:
            instance.subjects.add(subject)

        return instance
