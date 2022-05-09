"""" Student models """
from django.db import models


class Subject(models.Model):
    """ Subject model with basic fields """
    name = models.CharField(max_length=80)

    def __str__(self):
        return str(self.name)
