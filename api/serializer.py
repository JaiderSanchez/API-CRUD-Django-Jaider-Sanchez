from rest_framework import serializers
from .models import programmer

class ProgrammerSerializer(serializers.ModelSerializer):
    class Meta:
        model = programmer
        #fields = ('full_name', 'nickname', 'age')
        fields = '__all__'
        
class S