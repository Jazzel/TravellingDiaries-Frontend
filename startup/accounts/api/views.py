from .serializers import ProfileModelSerializer
from rest_framework import generics
from rest_framework import permissions
from accounts.models import Profile


class ProfilesListApiView(generics.ListAPIView):
    serializer_class = ProfileModelSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Profile.objects.all()
