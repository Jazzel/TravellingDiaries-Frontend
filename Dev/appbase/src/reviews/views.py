from django.shortcuts import render
from django.views.generic import (
    CreateView, UpdateView, DeleteView, DetailView, ListView)
from .models import Review

# Create your views here.


class ReviewListView(ListView):
    model = Review
    template_name = "dashboard/base.html"

    def get_context_data(self, **kwargs):
        context = super(ReviewListView, self).get_context_data(**kwargs)
        context['head'] = "Reviews"
        # context['title'] = "List"
        return context


class ReviewCreateView(CreateView):
    model = Review
    template_name = "dashboard/base.html"
    fields = ('rating', 'type', 'comments')

    def get_context_data(self, **kwargs):
        context = super(ReviewCreateView, self).get_context_data(**kwargs)
        context['head'] = "Reviews"
        context['title'] = "New"
        return context
