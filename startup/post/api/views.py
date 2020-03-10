from .serializers import PostModelSerializer
from rest_framework import generics
from rest_framework import permissions
from post.models import Post

from rest_framework import filters
from django.db.models import Q


class PostsListApiView(generics.ListAPIView):
    serializer_class = PostModelSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        query = self.request.query_params.get('query', None)
        if query:
            posts = Post.objects.filter(
                Q(message__icontains=query)
            ).prefetch_related('post_images')
        else:
            posts = Post.objects.all().prefetch_related('post_images')
        return posts
