from rest_framework import serializers
from .models import programmer
from .models import students

class ProgrammerSerializer(serializers.ModelSerializer):
    class Meta:
        model = programmer
        #fields = ('full_name', 'nickname', 'age')
        fields = '__all__'
        
class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = students
        #fields = ('full_name', 'nickname', 'age')
        fields = '__all__'