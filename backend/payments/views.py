from datetime import datetime
from unittest.mock import create_autospec
from urllib import request
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from payments.models import Payment
from rest_framework.viewsets import GenericViewSet
from .serializers import PaymentSerializer
import json as simplejson 

@api_view(['POST'])
def payment_create(self, request):
    """
    Create a payment.
    """
    if request.method == 'POST':
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
def proof_payment(request):
    
    """Payment verification"""
    
    if request.method == 'POST':
        serializer = PaymentSerializer(data=request.data)
        data = simplejson.loads(request.POST['data'])
        if Payment.objects.filter(token__exact = data.token).exists:
            payment = Payment.objects.get(token__exact = data.token)
            payment.is_paid = True
            payment.save()
            return Response(200, 'Payment verifyed')
        else:
            return Response(404, 'Payment not verifyed') 

        
        
        