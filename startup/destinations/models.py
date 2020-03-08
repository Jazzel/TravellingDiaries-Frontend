from django.db import models
from cities_light.models import City, Country
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField
from django.conf import settings

# Create your models here.
CATEGORY = (
    ('SP', 'Shopping'),
    ('NP', 'Nature & Parks'),
    ('MS', 'Museums'),
    ('LA', 'Landmarks'),
    ('MN', 'Monuments'),
    ('AG', 'Art Galleries'),
    ('WA', 'Water & Amusement Parks'),
)


class DestinationManager(models.Manager):
    def like_toggle(self, user, destination_obj):
        if user in destination_obj.liked.all():
            is_liked = False
            destination_obj.liked.remove(user)
        else:
            is_liked = True
            destination_obj.liked.add(user)
        return is_liked


class Destination(models.Model):
    name = models.CharField(max_length=500)
    city = models.ForeignKey(City, on_delete=models.CASCADE, default=0)
    category = models.CharField(choices=CATEGORY, max_length=100)
    description = models.TextField(blank=True)
    open_timing = models.TimeField(blank=True, null=True)
    close_timing = models.TimeField(blank=True, null=True)
    peak_time = models.TimeField(blank=True, null=True)
    location = models.URLField(blank=True)
    website = models.URLField(blank=True)
    contact = PhoneNumberField(blank=True, unique=True)
    email = models.EmailField(blank=True, unique=True)
    liked = models.ManyToManyField(
        settings.AUTH_USER_MODEL, blank=True, related_name='desination_liked')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('destinations:details', kwargs={'pk': self.pk})


class DestinationImage(models.Model):
    destination = models.ForeignKey(
        Destination, on_delete=models.CASCADE, default=None, related_name='destination_images')
    image = models.ImageField(upload_to='destination-images', blank=True)

    def __str__(self):
        return self.destination.name
#
