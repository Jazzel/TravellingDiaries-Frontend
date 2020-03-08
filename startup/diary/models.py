from django.db import models
from django.conf import settings

# Create your models here.


class Diary(models.Model):
    name = models.CharField(max_length=50)
    thumbnail = models.ImageField(upload_to='user_diaries')
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='user_diaries', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Diaries'
