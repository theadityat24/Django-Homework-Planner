from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.

class Subject(models.Model):
    teacher = models.CharField(max_length=50) 
    subject_title = models.CharField(max_length=75)
    period = models.CharField(max_length = 3)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.subject_title}'

class Assignment(models.Model):
    date_assigned = models.DateTimeField('date assigned', default=datetime.datetime.now)
    date_due = models.DateTimeField(
        'date due',
        default=datetime.datetime.now() + datetime.timedelta(days=1)
    )
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=300, blank=True, default="")
    PRIORITY_CHOICES = [
        (5, "Don't care"),
        (4, "Low"),
        (3, "Might as well"),
        (2, "Necessary"),
        (1, "Red Alert")
    ]
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.title}'
    


