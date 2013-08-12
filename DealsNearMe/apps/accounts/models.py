from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib.localflavor.us.models import USStateField


class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = USStateField()
    zipcode = models.CharField(max_length=15)
    favorite_color = models.CharField(max_length=255)
    latitude = models.IntegerField()
    longitude = models.IntegerField()


def user_post_save(sender, instance, created, **kwargs):
    if created is True:
        # We could create a user profile model here for our user
        # But we don't know any user profile information :(
        # We would have to override the save() in the User
        # creation form to pass extra attributes along, but at
        # that point we could just create the user there
        print "Post User Save Signal, instance: %s, kwargs: %s" % (instance, kwargs,)
post_save.connect(user_post_save, sender=User)
