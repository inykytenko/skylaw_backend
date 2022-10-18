from rest_framework import serializers
from divorcements.models import Divorcement, DivorcementChild
from django.core.exceptions import ValidationError 


class DivorcementSerializer(serializers.ModelSerializer):
    
    class Meta:
            model = Divorcement
            fields = '__all__'
            

class DivorcementChildSerializer(serializers.ModelSerializer):
    
    class Meta:
            model = DivorcementChild
            fields = '__all__'
    

