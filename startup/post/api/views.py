from django.utils.timesince import timesince
from rest_framework import viewsets
from rest_framework import status
from .serializers import PostModelSerializer
from rest_framework import permissions
from post.models import Post, PostImage
from .pagination import StandardResultPagination
from rest_framework import generics
from rest_framework import filters
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from django.urls import reverse_lazy

from rest_framework.parsers import MultiPartParser


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
        if not requested_user:
            queryset = Post.objects.all().prefetch_related('post_images').order_by("-created_at")
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
    queryset = Post.objects.all()
    serializer_class = PostModelSerializer

    # def create(self, request, *args, **kwargs):
    #     file_fields = list(request.FILES.keys())
    #     # print(file_fields)
    #     serializer = self.get_serializer(
    #         data=request.data, file_fields=file_fields)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)

    parser_classes = [MultiPartParser]

    def post(self, request, format=None):
        main_data = request.data
        post = Post.objects.create(
            user=self.request.user, message=main_data['message'], type=main_data['type'])
        post.save()
        post_id = post.id
        file_data = request.data.getlist('files')
        response_files_data = []

        for file in file_data:
            post_image = PostImage.objects.create(
                post=post,
                image=file
            )
            file_dic = {
                "id": post_image.id,
                "image": '/media/post-files/' + str(file),
                "post": post_id
            }
            response_files_data.append(file_dic)
            post_image.save()

        post_data = {
            'id': post.id,
            'user': {
                "username": self.request.user.username,
                "first_name": self.request.user.first_name,
                "last_name": self.request.user.last_name,
                "email": self.request.user.email,
                "url": reverse_lazy("user_profile", kwargs={'username': self.request.user.username})
            },
            'message': post.message,
            'type': post.type,
            'destination': '',
            'timesince': timesince(post.created_at) + " ago",
            'did_like': 0,
            'liked': post.liked.count(),
            'post_images': [file for file in response_files_data]
        }
        print(post_data)

        return Response(post_data)
