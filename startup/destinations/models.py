from django.db import models
# from django_countries.fields import CountryField
from cities_light.models import City, Country
from django.urls import reverse
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


class Destination(models.Model):
    name = models.CharField(max_length=500)
    city = models.ForeignKey(City, on_delete=models.CASCADE, default=0)
    description = models.TextField(blank=True)
    category = models.CharField(choices=CATEGORY, max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, blank=True)

    # def select_city(self, country):

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('destinations:details', kwargs={'pk': self.pk})
