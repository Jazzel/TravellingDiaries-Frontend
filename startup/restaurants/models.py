from django.db import models
from amenity.models import Amenity
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.


class RestaurantManager(models.Manager):
    def like_toggle(self, user, restaurant_obj):
        if user in restaurant_obj.liked.all():
            is_liked = False
            restaurant_obj.liked.remove(user)
        else:
            is_liked = True
            restaurant_obj.liked.add(user)
        return is_liked


class Restaurant(models.Model):
    name = models.CharField(max_length=250)
    location = models.URLField()
    amenities = models.ManyToManyField(Amenity)
    hotel_class = models.CharField(max_length=50)
    languages = models.CharField(max_length=500)
    style = models.CharField(max_length=500)
    rooms = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    liked = models.ManyToManyField(
        settings.AUTH_USER_MODEL, blank=True, related_name='restaurant_liked')
    website = models.URLField(blank=True)
    contact = PhoneNumberField(blank=True, unique=True)
    certificates = models.TextField(blank=True)
    special_diets = models.TextField(blank=True)
    cuisines = models.TextField(blank=True)
    meals = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, blank=True)

    objects = RestaurantManager()

    def __str__(self):
        return self.name

    # class Meta:
        # ordering = ["-timestamp"]


class RestaurantImage(models.Model):
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, default=None, related_name='restaurant_images')
    image = models.ImageField(upload_to='restaurant-images', blank=True)

    def __str__(self):
        return self.restaurant.name
