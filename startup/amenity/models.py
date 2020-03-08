from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.


class Amenity(models.Model):
    title = models.CharField(max_length=100)
    icon = models.CharField(max_length=100, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, blank=True)
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Amenities'
