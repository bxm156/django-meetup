from django.db import models
from django.contrib.auth.models import User
from django.contrib.localflavor.us.models import  USStateField, USPostalCodeField

class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = USStateField()
    zip = USPostalCodeField()
    latitude = models.IntegerField()
    longitude = models.IntegerField()