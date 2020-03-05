from django.urls import path
from .views import (ReviewListApiView, ReviewCreateApiView)
from django.contrib.auth import views as auth_views

app_name = 'reviews-api'

urlpatterns = [
    path('', ReviewListApiView.as_view(), name='list'),
    path('add/', ReviewCreateApiView.as_view(), name='add'),
    # path('edit/<int:pk>/', ReviewUpdateView.as_view(), name='edit'),
    # path('delete/<int:pk>/', ReviewDeleteView.as_view(), name='delete'),
    # path('details/<int:pk>/', ReviewDetailView.as_view(), name='details'),
    # path('profile/', auth_views..as_view(), name='profile'),
]
