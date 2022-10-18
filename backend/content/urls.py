from rest_framework import routers
from django.urls import path
from content.api import GetBlog, GetMainPage

router = routers.DefaultRouter()
router.register(r'blog', GetBlog, 'blog')
router.register(r'main_page', GetMainPage, 'main_page')


urlpatterns = router.urls
