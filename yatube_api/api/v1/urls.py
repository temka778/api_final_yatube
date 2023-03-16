from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import CommentViewSet, GroupViewSet, PostViewSet, FollowViewSet


ENDPOITS = [
    (r'posts', PostViewSet, 'posts'),
    (r'posts/(?P<post_id>[1-9]\d*)/comments', CommentViewSet, 'comments'),
    (r'groups', GroupViewSet, 'groups'),
    (r'follow', FollowViewSet, 'follow'),
]
router = DefaultRouter()
for endpoint, viewset, basename in ENDPOITS:
    router.register(endpoint, viewset, basename=basename)
URLS = [router.urls, 'djoser.urls', 'djoser.urls.jwt']
urlpatterns = []
for i in URLS:
    urlpatterns.append(path('', include(i)))
