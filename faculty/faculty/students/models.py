from django.db import models


# Create your models here.
class Student(models.Model):
    jmbg = models.CharField(max_length=13)
    index = models.CharField(max_length=10)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)