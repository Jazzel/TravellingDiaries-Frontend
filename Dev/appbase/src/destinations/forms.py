from django import forms
from .models import Destination


class DestinationModelForm(forms.ModelForm):
    class Meta:
        model = Destination
        fields = ['name', 'country', 'city', 'description']
