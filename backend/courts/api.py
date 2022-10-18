from rest_framework import viewsets, exceptions, pagination
from courts.serializers import RegionSerializer,CitySerializer, CourtSerializer
from rest_framework import status
from courts.models import Region,City,Court
from rest_framework.response import Response


class GetRegion(viewsets.ModelViewSet):
    serializer_class = RegionSerializer
    queryset = Region.objects.all()
    
    

class GetCity(viewsets.ModelViewSet):
    serializer_class = CitySerializer
    queryset = City.objects.all()
    
    
    def list(self, request):
        id=request.GET.get('region_id',3)
        city=City.objects.filter(region=id)
        city_serialized = CitySerializer(city, many=True).data
        return Response({
            "city":city_serialized
        })
        
class GetCourt(viewsets.ModelViewSet):
    serializer_class = CourtSerializer
    queryset = Court.objects.all()        