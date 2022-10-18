from re import T
from django.db import models
from tabnanny import verbose
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
import uuid
from django.utils import timezone
from django.db.models import DateTimeField
from datetime import datetime
# from payments.views import payment_create, proof_payment


def get_unique_token():
    """Generate unique token, checking the db for the duplicates"""
    while True:
        new_token = str(uuid.uuid4())    
        if not Payment.objects.filter(token__exact=new_token).exists():
            break
    return new_token

class Payment(models.Model):
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    payment_date = models.DateField(blank=True, null=True)
    is_paid = models.BooleanField()
    token = models.CharField(verbose_name="токен", max_length=16, blank=True, null=True)
    
    
    def __str__(self):
        return self.token
       
    def save(self, *args, **kwargs):
        self.token = get_unique_token()
        if self.is_paid == True:
            now = datetime.now()
            
                
    class Meta:
        verbose_name = "оплата"
        verbose_name_plural = "оплати" 