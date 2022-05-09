""" General configuration of Students app """
from django.apps import AppConfig


class StudentsConfig(AppConfig):
    """ Students configurations """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'crudalunos.students'
