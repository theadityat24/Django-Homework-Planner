from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets

from .serializers import UserSerializer, AssignmentSerializer, SubjectSerializer
from .models import Subject, Assignment
from django.contrib.auth.models import User

class BaseViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)

class SubjectViewSet(BaseViewSet):
    serializer_class = SubjectSerializer
    queryset = Subject.objects.all()

class AssignmentViewSet(BaseViewSet):
    serializer_class = AssignmentSerializer
    queryset = Assignment.objects.all()

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

