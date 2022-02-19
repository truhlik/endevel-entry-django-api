from django.shortcuts import render
from .models import Article, Tag
from rest_framework import viewsets, permissions, generics
from .serializers import ArticleSerializer, TagSerializer
from rest_framework.decorators import api_view
from django.http import JsonResponse


def _get_articles_by_name(name):
    result = Article.objects.filter(tags__name=name)
    return result


class ArticleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Articles to be viewed or edited.
    """
    queryset = Article.objects.all().order_by('-created_at')
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticated]


class TagViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Tags to be viewed or edited.
    """
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAuthenticated]


class ArticleByTagList(generics.ListAPIView):
    serializer_class = ArticleSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the name portion of the URL.
        """
        tag_name = self.kwargs["name"]
        print(tag_name)
        result = _get_articles_by_name(tag_name)
        return result


@api_view(['GET', 'POST'])
def articles_by_tag_name(request, name):
    if request.method == 'GET':
        print(name)
        return JsonResponse({"message": "Got some data!", "data": request.data})
    return JsonResponse({"message": "Hello, world!"}, safe=False)
