from django import views
from django.shortcuts import render
from django.urls import reverse_lazy
from accounts.forms import UserForm
from django.views.generic import (CreateView, TemplateView)
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin


def index(request):
    date = timezone.now()
    return render(request, 'home/base.html', context={'date': date.year})


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['head'] = "Dashboard"
        context['nbar'] = "Dashboard"
        return context


class SignUpView(CreateView):
    form_class = UserForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
