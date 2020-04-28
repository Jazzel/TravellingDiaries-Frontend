from django.urls import path
from django.conf.urls import url
from .views import (PostsListApiView, LikeToggleApiView, PostsCreateApiView)
from django.views.decorators.csrf import csrf_exempt

app_name = 'posts-api'
urlpatterns = [
    path('', PostsListApiView.as_view(), name='list'),
    path('create/', csrf_exempt(PostsCreateApiView.as_view()), name='create'),
    path('<slug:username>', PostsListApiView.as_view(), name='user_list'),
    path('<int:pk>/like/', LikeToggleApiView.as_view(), name='like-toggle'),

]
