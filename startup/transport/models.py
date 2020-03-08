from django.db import models
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
TYPE = (
    ('T', 'Train'),
    ('B', 'Bus'),
    ('P', 'Plane'),
)


class Transport(models.Model):
    name = models.CharField(max_length=250)
    # TODO ::
    type = models.CharField(choices=TYPE, max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.name

    # class Meta:
        # ordering = ["-timestamp"]


class TransportImage(models.Model):
    transport = models.ForeignKey(
        Transport, on_delete=models.CASCADE, default=None, related_name='transport_images')
    image = models.ImageField(upload_to='transport-images', blank=True)

    def __str__(self):
        return self.transport.name
