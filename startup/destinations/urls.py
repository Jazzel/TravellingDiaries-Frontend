from django.urls import path
from .views import (DestinationListView, DestinationCreateView,
                    DestinationDetailView, DestinationUpdateView,
                    DestinationDeleteView)

app_name = 'destinations'

urlpatterns = [
    path('', DestinationListView.as_view(), name='list'),
    path('add/', DestinationCreateView.as_view(), name='add'),
    path('edit/<int:pk>/', DestinationUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', DestinationDeleteView.as_view(), name='delete'),
    path('details/<int:pk>/', DestinationDetailView.as_view(), name='details'),
]
