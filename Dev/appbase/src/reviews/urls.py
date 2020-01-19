from django.urls import path
from .views import (ReviewListView, ReviewCreateView)
from django.contrib.auth import views as auth_views

app_name = 'reviews'

urlpatterns = [
    # path('<int:pk>/', UserDetailView.as_view(), name='details'),
    path('', ReviewListView.as_view(), name='list'),
    path('add/', ReviewCreateView.as_view(), name='add'),
    # path('profile/', auth_views..as_view(), name='profile'),

]
