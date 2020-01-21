from django.db import models
from django.urls import reverse_lazy
from django.conf import settings
from destinations.models import Destination
# Create your models here.


class Review(models.Model):
    Excellent = Families = '0'
    Good = Couples = '1'
    Average = Solo = '2'
    Poor = Business = '3'
    Terrible = Friends = '4'
    RATE = [
        (Excellent, 'Excellent'),
        (Good, 'Good'),
        (Average, 'Average'),
        (Poor, 'Poor'),
        (Terrible, 'Terrible'),
    ]
    TYPE = [
        (Families, 'Families'),
        (Couples, 'Couples'),
        (Solo, 'Solo'),
        (Business, 'Business'),
        (Friends, 'Friends'),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    destination = models.ForeignKey(
        Destination, on_delete=models.CASCADE)
    rating = models.CharField(
        max_length=32,
        choices=RATE,
        blank=False,
    )
    type = models.CharField(
        max_length=32,
        choices=TYPE,
        blank=False,
    )
    comments = models.TextField(blank=True)

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse_lazy('reviews:details', kwargs={'pk': self.pk})
