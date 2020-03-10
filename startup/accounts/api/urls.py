from django.urls import path
from .views import (ProfilesListApiView)
app_name = 'accounts-api'
urlpatterns = [
    path('', ProfilesListApiView.as_view(), name='list'),

]
