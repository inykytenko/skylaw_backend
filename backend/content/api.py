from pymongo import MongoClient
from rest_framework import viewsets, exceptions, pagination
from django.shortcuts import get_object_or_404
from content.serializers import BlogSerializerBase, BlogSerializerFull, BlogSerializerTranslations
from rest_framework.response import Response
from .models import Blog
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError


class BlogPaginator(pagination.PageNumberPagination):
    page_size = 12


class GetBlog(viewsets.ModelViewSet):
    queryset = Blog.objects.all().order_by('created_date')
    serializer_class = BlogSerializerBase
    pagination_class = BlogPaginator

    # def list(self, request):
    #     qs = self.queryset
    #     serializer = self.serializer_class(qs, many=True)
    #     return Response({
    #         'success': True,
    #         'blog': serializer.data,
    #     })

    def retrieve(self, request, pk=None, *args, **kwargs):
        queryset = Blog.objects.all()
        obj = get_object_or_404(queryset, translations__slug=pk)
        serializer = BlogSerializerFull(obj)

        prev_post = Blog.objects.filter(id__lt=obj.id).order_by('-id').first()
        prev_post_ser = BlogSerializerTranslations(prev_post).data

        next_post = Blog.objects.filter(id__gt=obj.id).order_by('id').first()
        next_post_ser = BlogSerializerTranslations(next_post).data

        return Response({
            'success': True,
            'prev': prev_post_ser,
            'next': next_post_ser,
            'post': serializer.data,
        })


def get_locale(request):
    locale_arg = request.GET.get('locale') or request.POST.get('locale')
    locale = 'ru' if locale_arg == 'ru' else 'uk'
    return locale


def get_homepage_collection(request):
    user = 'user'
    password = 'password'
    db_name = 'skylaw'
    connection_string = f'mongodb://{user}:{password}@localhost/{db_name}'
    mongo_client = MongoClient(connection_string)
    db = mongo_client[db_name]
    collection_name = 'home_page_' + get_locale(request)
    return db[collection_name]


class GetMainPage(viewsets.GenericViewSet):
    def list(self, request):
        resp = {
            'locale': get_locale(request),
            'blocks': {doc['_id']: doc for doc in get_homepage_collection(request).find()},
        }
        return Response(resp)
