from django.db import models

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length = 30)
    grade = models.IntegerField(max_length= 12, min_length = 9)
    age = models.IntegerField(max_length= 25)
