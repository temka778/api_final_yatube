from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, GroupViewSet, PostViewSet

ENDPOITS = [
    (r'posts', PostViewSet, 'posts'),
    (r'posts/(?P<post_id>[1-9]\d*)/comments', CommentViewSet, 'comments'),
    (r'groups', GroupViewSet, 'groups'),
]

router = DefaultRouter()

for endpoint, viewset, basename in ENDPOITS:
    router.register(endpoint, viewset, basename=basename)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
