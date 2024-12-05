#from django.shortcuts import render
from rest_framework import viewsets
from .serializer import ProgrammerSerializer
from .serializer import StudentsSerializer
from .models import programmer
from .models import students

# Create your views here.

class ProgrammerViewSet(viewsets.ModelViewSet):
    queryset = programmer.objects.all()
    serializer_class = ProgrammerSerializer
    
class StudentsViewSet(viewsets.ModelViewSet):
    queryset = students.objects.all()
    serializer_class = StudentsSerializer