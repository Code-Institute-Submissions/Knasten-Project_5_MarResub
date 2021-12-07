from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField

# Create your models here.


class UserProfile(models.Model):
    default_user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone_number = models.CharField(max_length=32, null=True, blank=True)
    default_country = CountryField(blank_label='Country*', null=True, blank=True)
    default_postcode = models.CharField(max_length=32, null=True, blank=True)
    default_town_or_city = models.CharField(max_length=64, null=True, blank=True)
    default_street_address = models.CharField(max_length=128, null=True, blank=True)
    default_street_address2 = models.CharField(max_length=128, null=True, blank=True)
    default_county = models.CharField(max_length=128, null=True, blank=True)

    def __str__(self):
        self.user.username
    


@receiver(post_save, sender=User)
def create_or_update_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    instance.userprofile.save()