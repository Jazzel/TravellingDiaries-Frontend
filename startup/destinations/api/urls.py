from django.urls import path
from .views import DestinationListApiView

app_name = 'destination-api'
urlpatterns = [
    path('', DestinationListApiView.as_view(), name='list'),

]
