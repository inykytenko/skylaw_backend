from rest_framework import routers
from courts.api import GetRegion,GetCity,GetCourt
from .views import HomePageView 
from django.urls import path
[
    
    path('', HomePageView.as_view(), name='home'), # homepage
    #path('admin/', admin.site.urls),
]

router = routers.DefaultRouter()
router.register('region',GetRegion,'courts-region' )
router.register('city',GetCity,'courts-city' )
router.register('courtfee',GetCourt, 'courts-courtfee')
urlpatterns = router.urls
