from django.urls import path
from . import views

urlpatterns = [
    path('', views.assignments, name="assignments"),
    path('class/', views.classWork, name="class_work"),
    path("ultra-secret/",views.ultraSecret, name ="ultraSecret")
]