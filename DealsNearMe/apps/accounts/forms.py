from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.localflavor.us.forms import USStateField, USStateSelect, USZipCodeField

from DealsNearMe.apps.accounts.models import UserProfile

from crispy_forms.layout import Submit, Layout, Field
from crispy_forms.helper import FormHelper
from geopy import geocoders


class UserRegistrationForm(UserCreationForm):
    address = forms.CharField(max_length=255, label='')
    city = forms.CharField(max_length=255, label='')
    state = USStateField(widget=USStateSelect, label='')
    zipcode = USZipCodeField(label='')

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit)
        address = self.cleaned_data['address']
        city = self.cleaned_data['city']
        state = self.cleaned_data['state']
        zipcode = self.cleaned_data['zipcode']
        g = geocoders.GoogleV3()
        place, (lat, lng) = g.geocode("%s, %s, %s %s" %(address, city, state, zipcode))
        user_profile = UserProfile(
            user=user,
            address=self.cleaned_data['address'],
            city=self.cleaned_data['city'],
            state=self.cleaned_data['state'],
            zip=self.cleaned_data['zipcode'],
            latitude=lat,
            longitude=lng,
        )
        user_profile.save()


class CrispyUserRegistrationForm(UserRegistrationForm):

    def __init__(self, request=None, *args, **kwargs):
        super(CrispyUserRegistrationForm, self).__init__(request, *args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-register'
        self.helper.form_method = 'post'
        self.helper.form_tag = True

        self.helper.layout = Layout(
                Field('username', label='', placeholder="Username"),
                Field('password1', label='', placeholder="Password"),
                Field('password2', label='', placeholder="Confirm Password"),
                Field('address', label='', placeholder="Address"),
                Field('city', label='', placeholder="City"),
                Field('state', label='', placeholder="State"),
                Field('zipcode', label='', placeholder="Zip"),
                Submit('submit', 'Register', css_class="btn-large")
        )
