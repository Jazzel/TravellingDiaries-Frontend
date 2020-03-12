from django.shortcuts import render
from django.views.generic import (CreateView, DetailView)
from startup.mixins import FormUserNeededMixin
from .models import Post, PostImage
from .forms import PostForm
from django.http import HttpResponse
from destinations.models import Destination
from django.forms.utils import ErrorList
from django import forms
from accounts.models import UserProfile
from django.shortcuts import redirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class PostDetailView(DetailView):
    model = Post
    queryset = Post.objects.all().prefetch_related('post_images')

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        following = UserProfile.objects.is_following(
            self.request.user, self.get_object())
        context['following'] = following
        context['head'] = 'Posts'
        context['sub_head'] = 'Details'
        return context


class PostCreateView(LoginRequiredMixin, CreateView):
    form_class = PostForm
    template_name = 'post/post_add.html'

    def get_context_data(self, **kwargs):
        context = super(PostCreateView, self).get_context_data(**kwargs)
        context['head'] = 'Posts'
        context['sub_head'] = 'Add'
        return context

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        user = self.request.user
        dest_name = self.request.POST.get('destinations')
        message = self.request.POST.get('message')
        images = request.FILES.getlist('images')

        if form.is_valid():
            if dest_name:
                try:
                    destination = Destination.objects.get(
                        name=dest_name)
                    if destination:
                        new_post = Post(
                            user=self.request.user,
                            message=message,
                            destination=destination
                        )
                        new_post.save()
                except ObjectDoesNotExist:
                    form._errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(
                        ['Destination you typed not found in our record'])
                    return self.form_invalid(form)
            else:

                new_post = Post(
                    user=user,
                    message=message
                )
                new_post.save()
            for image in images:
                image_form = PostImage.objects.create(
                    post=new_post)
                image_form.image = image
                image_form.save()

            return redirect('/posts/add/')

        else:
            return self.form_invalid(form)
