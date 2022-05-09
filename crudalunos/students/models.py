"""" Student models """
from django.db import models
from crudalunos.subjects.models import Subject


class Student(models.Model):
    """ Student model with basic fields """
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    joined_date = models.DateTimeField(auto_now_add=True)
    registration_number = models.CharField(max_length=10)
    subjects = models.ManyToManyField(Subject, blank=True)

    class Meta:
        """ Subject model meta config """
        ordering = ['-id']

    def __str__(self):
        return self.first_name + " " + self.last_name
