from sys import api_version
from rest_framework import viewsets, exceptions, pagination
from divorcements.serializers import DivorcementSerializer
from rest_framework import status
from divorcements.models import Divorcement
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view
from rest_framework import serializers

api_version = 1



class ChangeDivorcements(viewsets.ModelViewSet):
    serializer_class = DivorcementSerializer
    permission_class = AllowAny
    queryset = Divorcement.objects.none()
    
    def get_object(self, request, pk=None): 
        divorcement = Divorcement.objects.filter(token=pk).first()
        divorcement_serialized = DivorcementSerializer(divorcement, many=True).data
        return Response({
            "divorcement":divorcement_serialized
        })
        
      

    def create(self, request):
        token = request.data.get('token', '')
        step = request.data.get('step', '1')
        phone=request.data.get('phone')
        divorcement = 0
        if token:
            divorcement = Divorcement.objects.filter(token=token).first()
        if not divorcement:
            divorcement = Divorcement()
            divorcement.save()

        setattr(divorcement,"step_"+str(step),True)
        divorcement.save()

        # if re.match('^\+380\d{3}\d{2}\d{2}\d{2}$',phone):
        #     divorcements.first_person_telefon_number=phone
        #     divorcements.save()
        # else:
        #     raise ValidationError(
        #         {'detail': 'Невірний номер телефону'})

        return Response({
            'success': True,
            'token': divorcement.token,
        })

@api_view(['POST'])
    
def divorcement_create(request):
    """
    Create a divorcement.
    """
    if request.method == 'POST':
        # serializer = DivorcementSerializer(data=request.data)
        permission_class = AllowAny
        first_person_phone_number = request.data.get('userPhone', '')
        first_person_full_name = request.data.get('userName', '')
        first_person_tin = request.data.get('userRnokpp', '')
        first_person_zipcode = request.data.get('userRegion', '')
        first_person_city = request.data.get('userCity', '')
        first_person_street = request.data.get('userStreet', '')
        first_person_passport = request.data.get('userDocumentPassport', '')
        first_person_tin_file = request.data.get('userDocumentRnokpp', '')
        first_person_residence_certificate = request.data.get('userDocumentLocation', '')
        divorcement = 0

        if first_person_phone_number:
            divorcement = Divorcement.objects.filter(first_person_phone_number=first_person_phone_number).first()
        if not divorcement:
            divorcement = Divorcement()
            divorcement.save()
        
        setattr(divorcement,'first_person_phone_number',first_person_phone_number)
        divorcement.save()
        
        setattr(divorcement,'first_person_full_name',first_person_full_name)
        divorcement.save()
        
        setattr(divorcement,'first_person_tin',first_person_tin)
        divorcement.save()    
          
        setattr(divorcement,'first_person_zipcode',first_person_zipcode)
        divorcement.save() 
        
        setattr(divorcement,'first_person_city',first_person_city)
        divorcement.save() 
            
        setattr(divorcement,'first_person_street',first_person_street)
        divorcement.save() 
          
        setattr(divorcement,'first_person_passport',first_person_passport)
        divorcement.save() 
     
        setattr(divorcement,'first_person_tin_file',first_person_tin_file)
        divorcement.save()     
            
        setattr(divorcement,'first_person_residence_certificate',first_person_residence_certificate)
        divorcement.save() 

        if request.is_valid():
            # request.save()
            return Response(request.data, status=status.HTTP_201_CREATED)
        return Response(request.errors, status=status.HTTP_400_BAD_REQUEST)
    
    