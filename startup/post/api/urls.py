from django.urls import path
from django.conf.urls import url
from .views import (PostsListApiView, LikeToggleApiView)
app_name = 'posts-api'
urlpatterns = [
    path('', PostsListApiView.as_view(), name='list'),
    path('<slug:username>', PostsListApiView.as_view(), name='user_list'),
    path('<int:pk>/like/', LikeToggleApiView.as_view(), name='like-toggle'),

]
