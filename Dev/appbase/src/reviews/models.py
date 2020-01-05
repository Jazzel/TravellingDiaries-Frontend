from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Review(models.Model):

    RATE = [
        ('0', 'Excellent'),
        ('1', 'Good'),
        ('2', 'Average'),
        ('3', 'Poor'),
        ('4', 'Terrible'),
    ]
    TYPE = [
        ('0', 'Families'),
        ('1', 'Couples'),
        ('2', 'Solo'),
        ('3', 'Business'),
        ('4', 'Friends'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # destination = models.ForeignKey()
    rating = models.CharField(
        max_length=32,
        choices=RATE,
        blank=True,
    )
    type = models.CharField(
        max_length=32,
        choices=TYPE,
        blank=True,
    )
    comments = models.TextField(blank=True)
