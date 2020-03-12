from django.urls import path, include
from .views import (PostCreateView, PostDetailView)

app_name = 'posts'

urlpatterns = [
    # path('', FoodListView.as_view(), name='list'),
    path('add/', PostCreateView.as_view(), name='add'),
    # path('edit/<int:pk>/',
    #  FoodUpdateView.as_view(), name='edit'),
    # path('delete/<int:pk>/',
    #      FoodDeleteView.as_view(), name='delete'),
    path('details/<int:pk>/',
         PostDetailView.as_view(), name='details'),
]
