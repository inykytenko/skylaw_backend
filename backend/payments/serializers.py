from rest_framework.serializers import ModelSerializer

from .models import Payment

class PaymentSerializer(ModelSerializer):
    class Meta:
        model = Payment
        fields = (
            'amount', 'created_date', 'payment_date', 'is_paid', 'token'
        )