from django.contrib.auth.models import User
from .serializers import ReviewModelSerializer
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from django.db.models import Q
from rest_framework import permissions
# from .pagination import StandardResultPagination
from rest_framework.views import APIView
from rest_framework.response import Response
from reviews.models import Review


class ReviewCreateApiView(generics.CreateAPIView):
    serializer_class = ReviewModelSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ReviewListApiView(generics.ListAPIView):
    serializer_class = ReviewModelSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_context(self, *args, **kwargs):
        context = super(ReviewListApiView,
                        self).get_serializer_context(*args, **kwargs)
        context['request'] = self.request
        return context

    def get_queryset(self):
        requested_user = self.kwargs.get('username')
        if requested_user:
            queryset = Review.objects.filter(user__username=requested_user)
        else:
            queryset = Review.objects.filter(user=self.request.user)

        query = self.request.GET.get("q", None)
        if query is not None:
            queryset = queryset.filter(
                Q(content__icontains=query)
                | Q(user__username__icontains=query))
        return queryset
