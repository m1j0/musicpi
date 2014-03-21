from django.db import models
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
# Create your models here.

# http://localhost:8000


class Title(models.Model):
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to=os.path.join(BASE_DIR, 'music_files'))
    val = models.IntegerField()

    def __str__(self):
        return self.name


class Interpreter(models.Model):
    name = models.CharField(max_length=100)
    interpreter = models.ManyToManyRel(Title)

    def __str__(self):
        return self.name
