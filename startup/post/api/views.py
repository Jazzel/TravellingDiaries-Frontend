from .serializers import PostModelSerializer
from rest_framework import permissions
from post.models import Post
from .pagination import StandardResultPagination
from rest_framework import generics
from rest_framework import filters
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response


class LikeToggleApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk, format=None):
        posts_qs = Post.objects.filter(pk=pk)
        message = "Not allowed"
        if request.user.is_authenticated:
            is_liked = Post.objects.like_toggle(
                request.user, posts_qs.first())
            likes = posts_qs.first().liked.all().count()
            return Response({'liked': is_liked, 'likes': likes})
        return Response({'message': message}, status=400)


class PostsListApiView(generics.ListAPIView):
    serializer_class = PostModelSerializer
    pagination_class = StandardResultPagination

    def get_serializer_context(self, *args, **kwargs):
        context = super(PostsListApiView, self).get_serializer_context(
            *args, **kwargs)
        context['request'] = self.request
        return context

    def get_queryset(self):
        requested_user = self.kwargs.get('username')
        if requested_user:
            queryset = Post.objects.filter(
                user__username=requested_user).prefetch_related('post_images').order_by("-created_at")
        else:
            im_following = self.request.user.profile.get_following()
            qs1 = Post.objects.filter(
                user__in=im_following).prefetch_related('post_images')
            qs2 = Post.objects.filter(
                user=self.request.user).prefetch_related('post_images')
            queryset = (qs1 | qs2).distinct().order_by("-created_at")

        query = self.request.GET.get("q", None)
        if query is not None:
            queryset = queryset.filter(
                Q(content__icontains=query) | Q(
                    user__username__icontains=query)
            )
        return queryset


class PostsCreateApiView(generics.CreateAPIView):
    serializer_class = PostModelSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
