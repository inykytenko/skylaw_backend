from rest_framework import serializers 
from courts.models import Region,City, Court


class RegionSerializer(serializers.ModelSerializer):

    class Meta:
            model = Region
            fields = '__all__'

class CitySerializer(serializers.ModelSerializer):

    class Meta:
            model = City
            fields = '__all__'
            
class CourtSerializer(serializers.ModelSerializer):

    class Meta:
            model = Court
            fields = '__all__'           