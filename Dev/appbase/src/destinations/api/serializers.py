from rest_framework import serializers
from django.urls import reverse_lazy
from destinations.models import Destination


class DestinationDisplaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Destination
        fields = [
            'name',
        ]
