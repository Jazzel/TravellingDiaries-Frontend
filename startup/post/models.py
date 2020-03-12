from destinations.models import Destination
from django.db import models
from django.urls import reverse
from django.conf import settings
from groups.models import Group
import misaka
from django.contrib.auth import get_user_model
User = get_user_model()


class PostManager(models.Manager):
    def like_toggle(self, user, post_obj):
        if user in post_obj.liked.all():
            is_liked = False
            post_obj.liked.remove(user)
        else:
            is_liked = True
            post_obj.liked.add(user)
        return is_liked


# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User, related_name='posts',
                             on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    message = models.TextField(blank=True)
    message_html = models.TextField(editable=False)
    group = models.ForeignKey(
        Group, related_name='posts', null=True, blank=True, on_delete=models.CASCADE)
    liked = models.ManyToManyField(
        settings.AUTH_USER_MODEL, blank=True, related_name='post_liked')
    updated = models.DateTimeField(auto_now=True, blank=True)
    destination = models.ForeignKey(
        Destination, on_delete=models.CASCADE, blank=True, null=True)

    objects = PostManager()

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        self.message_html = misaka.html(self.message)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('posts:add')

    class Meta:
        ordering = ['-created_at']


class PostImage(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, default=None, related_name='post_images')
    image = models.FileField(upload_to='post-files', blank=True)

    def __str__(self):
        return self.post.message
#
