from django.urls import path, include, re_path
from .models import Payment
from payments import views
from rest_framework.routers import DefaultRouter
from .views import api_view
from rest_framework.urlpatterns import format_suffix_patterns

router = DefaultRouter()
router.register(Payment, api_view, 'payment')

urlpatterns = [
   # path('', PaymentListView.as_view(), name = 'payment-list-view'),
    path('create/',views.payment_create),
    # path('token/', ),
    #path('view1/', MyView.as_view()),
    #re_path('^', include(router.urls)),
    path('proof/',views.proof_payment),
]
