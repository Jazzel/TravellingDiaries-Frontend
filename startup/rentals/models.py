from django.db import models
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
TYPE = (
    ('A', 'Apparment'),
    ('B', 'Bungalow'),
    ('C', 'Cottage'),
)


class Rental(models.Model):
    name = models.CharField(max_length=250)
    # TODO ::
    type = models.CharField(choices=TYPE, max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.name

    # class Meta:
        # ordering = ["-timestamp"]


class RentalImage(models.Model):
    rental = models.ForeignKey(
        Rental, on_delete=models.CASCADE, default=None, related_name='rental_images')
    image = models.ImageField(upload_to='rental-images', blank=True)

    def __str__(self):
        return self.rental.name
