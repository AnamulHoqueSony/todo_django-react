from django.shortcuts import render
from rest_framework import viewsets          # add this
from .serializers import TodoSerializer      # add this
from .models import Todo                     # add this
#write view code here
class TodoView(viewsets.ModelViewSet):       # add this
      serializer_class = TodoSerializer          # add this
      queryset = Todo.objects.all()
