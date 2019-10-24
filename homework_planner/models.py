from django.db import models
import datetime
# Create your models here.

class Subject(models.Model):
    teacher = models.CharField(max_length=50) 
    subject_title = models.CharField()
    period = models.CharField(max_length = 3)

class Assignment(models.Model):
    date_assigned = models.DateTimeField('date assigned', default=datetime.datetime.now)
    date_due = models.DateTimeField(
        'date due',
        default=datetime.datetime.now() + datetime.timedelta(days=1)
    )
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    PRIORITY_CHOICES = [
        (5, "A"),
        (4, "B"),
        (3, "C"),
        (2, "D"),
        (1, "F")
    ]
    priority = models.IntegerField(choices=PRIORITY_CHOICES)




    
    
