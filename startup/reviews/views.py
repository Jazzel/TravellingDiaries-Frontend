from django.shortcuts import render
from django.views.generic import (
    CreateView, UpdateView, DeleteView, DetailView, ListView)
from .models import Review
from startup.mixins import FormUserNeededMixin
from .forms import ReviewModelForm
# Create your views here.


class ReviewListView(ListView):
    model = Review

    def get_context_data(self, **kwargs):
        context = super(ReviewListView, self).get_context_data(**kwargs)
        context['head'] = "Reviews"
        context['title'] = "List"
        return context


class ReviewCreateView(FormUserNeededMixin, CreateView):
    form_class = ReviewModelForm
    template_name = 'reviews/review_add.html'

    def get_context_data(self, **kwargs):
        context = super(ReviewCreateView, self).get_context_data(**kwargs)
        context['head'] = "Reviews"
        context['title'] = "New"
        return context


class ReviewUpdateView(UpdateView):
    model = Review
    form_class = ReviewModelForm
    template_name = 'reviews/review_edit.html'

    def get_context_data(self, **kwargs):
        context = super(ReviewUpdateView, self).get_context_data(**kwargs)
        context['head'] = "Reviews"
        context['title'] = "Edit"
        return context


class ReviewDeleteView(DeleteView):
    model = Review
    success_url = 'reviews:list'

    def get_context_data(self, **kwargs):
        context = super(ReviewDeleteView, self).get_context_data(**kwargs)
        context['head'] = "Reviews"
        context['title'] = "Remove"
        return context


class ReviewDetailView(DetailView):
    model = Review

    def get_context_data(self, **kwargs):
        context = super(ReviewDetailView, self).get_context_data(**kwargs)
        context['head'] = "Reviews"
        context['title'] = "Details"
        return context
