from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, GroupViewSet, PostViewSet, FollowViewSet

ENDPOITS = [
    (r'posts', PostViewSet, 'posts'),
    (r'posts/(?P<post_id>[1-9]\d*)/comments', CommentViewSet, 'comments'),
    (r'groups', GroupViewSet, 'groups'),
    (r'follow', FollowViewSet, 'follow'),
]

router_v1 = DefaultRouter()

for endpoint, viewset, basename in ENDPOITS:
    router_v1.register(endpoint, viewset, basename=basename)

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
