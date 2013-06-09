from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.localflavor.us.forms import USStateField, USStateSelect, USZipCodeField

from DealsNearMe.apps.accounts.models import UserProfile

from geopy import geocoders


class UserRegistrationForm(UserCreationForm):
    address = forms.CharField(max_length=255)
    city = forms.CharField(max_length=255)
    state = USStateField(widget=USStateSelect)
    zip = USZipCodeField()

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit)
        address = self.cleaned_data['address']
        city = self.cleaned_data['city']
        state = self.cleaned_data['state']
        zip = self.cleaned_data['zip']
        g = geocoders.GoogleV3()
        place, (lat, lng) = g.geocode("%s, %s, %s %s" %( address, city, state, zip))
        user_profile = UserProfile(
            user=user,
            address=self.cleaned_data['address'],
            city=self.cleaned_data['city'],
            state=self.cleaned_data['state'],
            zip=self.cleaned_data['zip'],
            latitude=lat,
            longitude=lng,
        )
        user_profile.save()
