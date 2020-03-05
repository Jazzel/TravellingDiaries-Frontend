from django.shortcuts import render
from django.views.generic import (CreateView, UpdateView, DeleteView,
                                  DetailView, ListView)
from .models import Destination
from startup.mixins import FormUserNeededMixin
from .forms import DestinationModelForm
# Create your views here.


class DestinationListView(ListView):
    model = Destination

    def get_context_data(self, **kwargs):
        context = super(DestinationListView, self).get_context_data(**kwargs)
        context['head'] = "Destinations"
        context['title'] = "List"
        return context


class DestinationCreateView(CreateView):
    form_class = DestinationModelForm
    template_name = 'destinations/destination_add.html'

    def get_context_data(self, **kwargs):
        context = super(DestinationCreateView, self).get_context_data(**kwargs)
        context['head'] = "Destinations"
        context['title'] = "New"
        return context


class DestinationDetailView(DetailView):
    model = Destination

    def get_context_data(self, **kwargs):
        context = super(DestinationDetailView, self).get_context_data(**kwargs)
        context['head'] = "Destinations"
        context['title'] = "Details"
        return context


class DestinationUpdateView(UpdateView):
    model = Destination
    form_class = DestinationModelForm
    template_name = "destinations/destination_edit.html"

    def get_context_data(self, **kwargs):
        context = super(DestinationUpdateView, self).get_context_data(**kwargs)
        context['head'] = "Destinations"
        context['title'] = "Edit"
        return context


class DestinationDeleteView(DeleteView):
    model = Destination
    success_url = 'destinations:list'

    def get_context_data(self, **kwargs):
        context = super(DestinationDeleteView, self).get_context_data(**kwargs)
        context['head'] = "Destinations"
        context['title'] = "Remove"
        return context
