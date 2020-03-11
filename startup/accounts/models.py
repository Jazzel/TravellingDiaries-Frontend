from django.db import models
from django.conf import settings
from django.urls import reverse
from django_countries.fields import CountryField
from django.db.models import Sum
from django.db.models.signals import post_save
from django.shortcuts import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.signals import user_logged_in, user_logged_out
import datetime
from django.urls import reverse_lazy
import logging
from django.dispatch import receiver
User = get_user_model()
# Create your models here.


ADDRESS_CHOICES = (
    ('B', 'Billing'),
    ('S', 'Shipping'),
)


class UserProfileManager(models.Manager):
    use_for_related_fields = True

    def all(self):
        qs = self.get_queryset().all()
        try:
            if self.instance:
                qs = qs.exclude(user=self.instance)
        except:
            pass
        return qs

    def toggle_follow(self, user, to_toggle_user):
        user_profile, created = UserProfile.objects.get_or_create(
            user=user)
        if to_toggle_user in user_profile.following.all():
            user_profile.following.remove(to_toggle_user)
            added = False
        else:
            user_profile.following.add(to_toggle_user)
            added = True
        return added

    def is_following(self, user, followed_by_user):
        user_profile, created = UserProfile.objects.get_or_create(user=user)
        if created:
            return False
        if followed_by_user in user_profile.following.all():
            return True
        return False

class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, related_name='profile', on_delete=models.CASCADE)
    following = models.ManyToManyField(
        settings.AUTH_USER_MODEL, blank=True, related_name='followed_by')
    bio = models.TextField(max_length=500, blank=True)
    image = models.ImageField(upload_to='user-images', blank=True)
    stripe_customer_id = models.CharField(max_length=50, blank=True, null=True)
    one_click_purchasing = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, blank=True)

    objects = UserProfileManager()

    def __str__(self):
        return self.user.username

    def get_following(self):
        user = self.following.all()
        return user.exclude(username=self.user.username)

    def get_absolute_url(self):
        return reverse_lazy('user_profile', kwargs={"username": self.user.username})

    def get_follow_url(self):
        return reverse_lazy('profiles:follow', kwargs={"username": self.user.username})


class UserLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    session_key = models.CharField(max_length=100, blank=False, null=False)
    host = models.CharField(max_length=100, blank=False, null=False)
    login_time = models.DateTimeField(blank=True, null=True)
    logout_time = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.user.username


class Address(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    street_address = models.CharField(max_length=100)
    apartment_address = models.CharField(max_length=100)
    country = CountryField(multiple=False)
    zip = models.CharField(max_length=100)
    address_type = models.CharField(max_length=1, choices=ADDRESS_CHOICES)
    default = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = 'Addresses'


# for logging - define "error" named logging handler and logger in settings.py
error_log = logging.getLogger('error')


@receiver(user_logged_in)
def log_user_logged_in(sender, user, request, **kwargs):
    try:
        login_logout_logs = UserLog.objects.filter(
            session_key=request.session.session_key, user=user.id)[:1]
        if not login_logout_logs:
            login_logout_log = UserLog(login_time=datetime.datetime.now(
            ), session_key=request.session.session_key, user=user, host=request.META['HTTP_HOST'])
            login_logout_log.save()
    except Exception:
        # log the error
        error_log.error(
            "log_user_logged_in request: %s, error: %s" % (request))


@receiver(user_logged_out)
def log_user_logged_out(sender, user, request, **kwargs):
    try:
        login_logout_logs = UserLog.objects.filter(
            session_key=request.session.session_key, user=user.id, host=request.META['HTTP_HOST'])
        login_logout_logs.filter(logout_time__isnull=True).update(
            logout_time=datetime.datetime.now())
        if not login_logout_logs:
            login_logout_log = UserLog(logout_time=datetime.datetime.now(
            ), session_key=request.session.session_key, user=user, host=request.META['HTTP_HOST'])
            login_logout_log.save()
    except Exception:
        # log the error
        error_log.error(
            "log_user_logged_out request: %s, error: %s" % (request))


def userprofile_receiver(sender, instance, created, *args, **kwargs):
    if created:
        userprofile = UserProfile.objects.create(user=instance)


post_save.connect(userprofile_receiver, sender=settings.AUTH_USER_MODEL)
