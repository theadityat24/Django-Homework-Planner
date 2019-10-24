from rest_framework import serializers
from .models import Subject, Assignment
from django.contrib.auth.models import User

class SubjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Subject
        fields = ['teacher', 'subject_title', 'period', 'user']
        
class AssignmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Assignment
        fields = [
            'date_assigned',
            'date_due',
            'subject',
            'title',
            'description',
            'priority',
            'user',
        ]

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'password'
        ]