from rest_framework import routers
from divorcements.api import ChangeDivorcements
from divorcements import views
from django.urls import path, include, re_path

router = routers.DefaultRouter()
router.register('divorcements',ChangeDivorcements,'divorcements-changedivorcement' )
#router.register('divorcements',)

urlpatterns = [
   # path('upload/', views.image_upload_view),
    #path('create/', ChangeDivorcements),
    # path(f'api/v{api_version}/', include(router.urls)),
    #path('divorcements/<int:pk>/', ChangeDivorcements, name='get_object')
   
    
]
