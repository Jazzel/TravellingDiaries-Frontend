from django.shortcuts import render
from django.views.generic import (DetailView, CreateView, TemplateView)
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
User = get_user_model()


class ProfileView(LoginRequiredMixin, TemplateView):
    def get_queryset(self):
        queryset = User.objects.get(username=self.request.user.username)
        return queryset
    template_name = 'accounts/user_detail.html'
