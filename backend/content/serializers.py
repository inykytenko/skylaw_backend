from rest_framework import serializers
from django.contrib.auth.models import User
from parler_rest.serializers import TranslatableModelSerializer, TranslatedFieldsField
from content.models import Blog


class BlogSerializerTranslations(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Blog)

    class Meta:
        model = Blog
        fields = ['translations']


class BlogSerializerBase(BlogSerializerTranslations):

    author_name = serializers.SerializerMethodField()
    created_date = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        fields = BlogSerializerTranslations.Meta.fields + [ 'created_date', 'author_name', 'image']

    def get_author_name(self, obj):
        if obj.author:
            return obj.author.first_name + ' ' + obj.author.last_name
        return ''

    def get_created_date(self, obj):
        if obj.created_date:
            return obj.created_date.strftime("%d.%m.%Y")
        return ''



class BlogSerializerFull(BlogSerializerBase):

    class Meta:
        model = Blog
        fields = BlogSerializerBase.Meta.fields
        depth = 1
