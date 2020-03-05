from phonenumber_field.modelfields import PhoneNumberField
from django.conf import settings
from amenity.models import Amenity
from django.db import models

# Create your models here.


class PackageManager(models.Manager):
    def like_toggle(self, user, package_obj):
        if user in package_obj.liked.all():
            is_liked = False
            package_obj.liked.remove(user)
        else:
            is_liked = True
            package_obj.liked.add(user)
        return is_liked


class Package(models.Model):
    name = models.CharField(max_length=250)
    liked = models.ManyToManyField(
        settings.AUTH_USER_MODEL, blank=True, related_name='package_liked')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, blank=True)

    objects = PackageManager()

    def __str__(self):
        return self.name

    # class Meta:
        # ordering = ["-timestamp"]


class PackageImage(models.Model):
    package = models.ForeignKey(
        Package, on_delete=models.CASCADE, default=None, related_name='package_images')
    image = models.ImageField(upload_to='package-images', blank=True)

    def __str__(self):
        return self.package.name
