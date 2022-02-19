from django.contrib.auth.models import User, Group
from .models import Article, Tag
from rest_framework import serializers


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Article
        fields = ['title_cz', 'title_en', 'content_cz',
                  'content_en', 'header_image', 'header_thumb', 'tags']


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ['name']
