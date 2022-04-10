from .models import Article, Tag
from rest_framework import viewsets, permissions, generics
from .serializers import ArticleSerializer, TagSerializer
from django.conf import settings
import os
import environ


def _get_articles_by_name(name):
    result = Article.objects.filter(tags__name=name)
    return result


class ArticleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Articles to be viewed or edited.
    """
    queryset = Article.objects.all().order_by('-created_at')
    serializer_class = ArticleSerializer


class TagViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Tags to be viewed or edited.
    """
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class ArticleByTagList(generics.ListAPIView):
    serializer_class = ArticleSerializer

    def get_queryset(self):
        """
        This view should return a list of all the articles for given tag name.
        """
        tag_name = self.kwargs["name"]
        result = _get_articles_by_name(tag_name)
        return result
