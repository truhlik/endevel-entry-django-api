from django.urls import include, path
from rest_framework import routers
from . import views
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'articles', views.ArticleViewSet)
router.register(r'tags', views.TagViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('articles/<str:name>', views.ArticleByTagList.as_view(),
         name="article_by_tag_list"),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]


urlpatterns += static(settings.UPLOAD_URL,
                      document_root=settings.UPLOAD_ROOT)
