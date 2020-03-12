from .serializers import DestinationDisplaySerializer
from destinations.models import Destination
from rest_framework import generics
from destinations.models import Destination


class DestinationListApiView(generics.ListAPIView):
    serializer_class = DestinationDisplaySerializer
    queryset = Destination.objects.all()
