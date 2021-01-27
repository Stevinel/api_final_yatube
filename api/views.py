from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from .models import Group, Post
from .permissions import IsAuthorOrReadOnlyPermission
from .serializers import (
    CommentSerializer,
    FollowSerializer,
    GroupSerializer,
    PostSerializer,
)


class PostViewSet(ModelViewSet):
    permission_classes = [
        IsAuthenticatedOrReadOnly,
        IsAuthorOrReadOnlyPermission,
    ]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        "group",
    ]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(ModelViewSet):
    permission_classes = [
        IsAuthenticatedOrReadOnly,
        IsAuthorOrReadOnlyPermission,
    ]
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, post_id=self.kwargs.get("post_id"))

    def get_queryset(self):
        post = get_object_or_404(Post, pk=self.kwargs.get("post_id"))
        return post.comments.all()


class GroupViewSet(CreateModelMixin, ListModelMixin, GenericViewSet):

    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class FollowViewSet(CreateModelMixin, ListModelMixin, GenericViewSet):

    permission_classes = [IsAuthenticated]
    serializer_class = FollowSerializer
    filter_backends = [SearchFilter]
    search_fields = ["=following__username", "user__username"]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return self.request.user.following.all()
