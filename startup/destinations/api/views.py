from .serializers import DestinationDisplaySerializer
from destinations.models import Destination
from rest_framework import generics
from destinations.models import Destination


class DestinationListApiView(generics.ListAPIView):
    serializer_class = DestinationDisplaySerializer

    def get_queryset(self):
        query = self.request.query_params.get('query', None)
        print(query)
        if query:
            destinations = Destination.objects.filter(category=query)
        else:
            destinations = Destination.objects.all()
        return destinations
