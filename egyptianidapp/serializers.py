from rest_framework import serializers
from .models import NationalID
from .validation import NationalIDValidation

class NationalIDSerializer(serializers.ModelSerializer):
    status = serializers.CharField(read_only=True)
    class Meta:
        model = NationalID
        fields = ['number', 'birth_date' , 'status' , 'location']  
        extra_kwargs = {
            'birth_date': {'read_only': True}  ,
            'location': {'read_only': True}
        }
