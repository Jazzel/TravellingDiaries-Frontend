from . import views
from django.urls import path

app_name = 'weather'

urlpatterns = [
    path('', views.index),  # the path for our index view
]
