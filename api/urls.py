from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

router = DefaultRouter()
router.register("follow", FollowViewSet, basename="Follow")
router.register("group", GroupViewSet, basename="Groups")
router.register("posts", PostViewSet, basename="Posts")
router.register(
    r"posts/(?P<post_id>\d+)/comments", CommentViewSet, basename="Comments"
)

urlpatterns = [
    path("v1/", include(router.urls)),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
