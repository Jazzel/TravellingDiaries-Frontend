from django.urls import path
from .views import (ReviewListView, ReviewCreateView, ReviewUpdateView,
                    ReviewDeleteView, ReviewDetailView)

app_name = 'reviews'

urlpatterns = [
    path('', ReviewListView.as_view(), name='list'),
    path('add/', ReviewCreateView.as_view(), name='add'),
    path('edit/<int:pk>/', ReviewUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', ReviewDeleteView.as_view(), name='delete'),
    path('details/<int:pk>/', ReviewDetailView.as_view(), name='details'),
    # path('profile/', auth_views..as_view(), name='profile'),
]
