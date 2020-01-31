from django.db import models
# from django_countries.fields import CountryField
from cities_light.models import City, Country
from django.urls import reverse
# Create your models here.


class Destination(models.Model):
    name = models.CharField(max_length=500)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, default=0)
    city = models.ForeignKey(City, on_delete=models.CASCADE, default=0)
    description = models.TextField(blank=True)

    # def select_city(self, country):
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('destinations:details', kwargs={'pk': self.pk})