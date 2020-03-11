"""startup URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import HomeView
from accounts.views import MyProfileView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('<slug:username>', MyProfileView.as_view(), name='user_profile'),

    path('accounts/', include('allauth.urls')),
    path('account/', include('accounts.urls', namespace='profiles')),
    path('posts/', include('post.urls', namespace='posts')),
    path('api/posts/', include('post.api.urls', namespace='posts-api')),
    path('reviews/', include('reviews.urls', namespace='reviews')),
    path('destinations/', include('destinations.urls',
                                  namespace='destinations')),
]
if settings.DEBUG:
    urlpatterns += (static(settings.STATIC_URL,
                           document_root=settings.STATIC_ROOT))
    urlpatterns += (static(settings.MEDIA_URL,
                           document_root=settings.MEDIA_ROOT))
