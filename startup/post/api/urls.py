from django.urls import path
from django.conf.urls import url
from .views import (PostsListApiView)
app_name = 'posts-api'
urlpatterns = [
    # path('', PostsListApiView.as_view(), name='list'),
    url(r'^$',
        PostsListApiView.as_view(), name='list'),

]
