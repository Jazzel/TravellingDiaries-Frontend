from django import views
from django.shortcuts import render
from django.urls import reverse_lazy
from accounts.forms import UserForm
from django.views.generic import (CreateView)
from django.utils import timezone


def index(request):
    date = timezone.now()
    return render(request, 'home/base.html', context={'date': date.year})


class SignUpView(CreateView):
    form_class = UserForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
