from django.shortcuts import render
import io
from urllib import request
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from divorcements.models import Divorcement, DivorcementChild
from .serializers import DivorcementSerializer 
from rest_framework.permissions import AllowAny
from django.shortcuts import render

  
#@api_view(['POST'])
#def divorcement_create(request):
    #"""
   # Create a divorcement.
   # """
    #if request.method == 'POST':
      #  serializer = DivorcementSerializer(data=request.data)
      #  permission_class = AllowAny
      #  if serializer.is_valid():
      #      serializer.save()
      #      return Response(serializer.data, status=status.HTTP_201_CREATED)
      #  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
   # 