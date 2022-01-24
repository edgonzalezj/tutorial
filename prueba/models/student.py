from django.db import models

class Studient(models.Model):
    name = models.CharField(max_length=200)
    birthday = models.DateTimeField('date published')
