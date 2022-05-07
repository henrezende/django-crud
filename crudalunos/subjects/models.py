from django.db import models

# Create your models here.

class Subject(models.Model):
    """ Subject model with basic fields """
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name
