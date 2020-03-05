from django import forms
from .models import Review


class ReviewModelForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['destination', 'rating', 'type', 'comments']
