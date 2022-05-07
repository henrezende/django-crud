from django.db import models

from crudalunos.subjects.models import Subject

# Create your models here.

class Student(models.Model):
    """ Student model with basic fields """
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    joined_date = models.DateTimeField(auto_now_add=True)
    registration_number = models.CharField(max_length=10)
    subjects = models.ManyToManyField(Subject)

    def __str__(self):
        return self.first_name
