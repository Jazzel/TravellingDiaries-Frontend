from django.urls import path
from .views import (ProfileView)
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
    # path('<int:pk>/', UserDetailView.as_view(), name='details'),
    path('profile/', ProfileView.as_view(), name='profile'),
    # path('profile/', auth_views..as_view(), name='profile'),

]
