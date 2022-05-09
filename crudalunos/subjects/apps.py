""" General configuration of Subjects app """
from django.apps import AppConfig


class SubjectsConfig(AppConfig):
    """ Subjects configurations """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'crudalunos.subjects'
