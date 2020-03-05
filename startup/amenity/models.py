from django.db import models

# Create your models here.


class Amenity(models.Model):
    title = models.CharField(max_length=100)
    icon = models.CharField(max_length=100, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Amenities'
