from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    destinations = forms.TextInput(
        attrs={'id': 'destination', 'name': 'destination'})
    images = forms.FileField(required=False,
                             widget=forms.ClearableFileInput(attrs={'multiple': True, 'class': 'form-control pb-5', 'required': False}))

    class Meta:
        model = Post
        fields = ['message', 'images', ]
