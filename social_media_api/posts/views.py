from rest_framework import viewsets, permissions
from .models import Post, Comment, Like
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from notifications.models import Notification
from .serializers import PostSerializer, CommentSerializer
from rest_framework import filters

Post.objects.filter(author__in=following_users).order_by
following.all()

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_post(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
        like, created = Like.objects.get_or_create(post=post, user=request.user)
        if created:
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb='liked your post',
                target=post
            )
            return Response({"detail": "Post liked."}, status=201)
        else:
            return Response({"detail": "Post already liked."}, status=400)
    except Post.DoesNotExist:
        return Response({"detail": "Post not found."}, status=404)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def unlike_post(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
        Like.objects.filter(post=post, user=request.user).delete()
        return Response({"detail": "Post unliked."}, status=200)
    except Post.DoesNotExist:
        return Response({"detail": "Post not found."}, status=404)
