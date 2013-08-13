from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.localflavor.us.forms import USStateField, USStateSelect, USZipCodeField

from crispy_forms.layout import Submit, Layout, Field
from crispy_forms.helper import FormHelper
from geopy import geocoders


class UserRegistrationForm(forms.ModelForm):

    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)

    # Since we are saving the lat and long in clean..
    latitude = forms.IntegerField(required=False)
    longitude = forms.IntegerField(required=False)

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name',
                'address', 'city', 'state', 'zipcode', 'favorite_color')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Password mismatch")
        return password2

    def clean(self):
        cleaned_data = super(UserRegistrationForm, self).clean()
        g = geocoders.GoogleV3()
        place, (lat, lng) = g.geocode("%s, %s, %s %s" %(
            cleaned_data['address'],
            cleaned_data['city'],
            cleaned_data['state'],
            cleaned_data['zipcode']
        ))
        self.cleaned_data['latitude'] = lat
        self.cleaned_data['longitude'] = lng
        return self.cleaned_data

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        user.latitude = self.cleaned_data['latitude']
        user.longitude = self.cleaned_data['longitude']
        if commit:
            user.save()
        return user


class CrispyUserProfileForm(forms.ModelForm):
    #We still want to use custom widgets
    state = USStateField(widget=USStateSelect, label='')
    zipcode = USZipCodeField(label='')

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'address', 'city', 'state', 'zipcode', 'favorite_color']

    def __init__(self, request=None, *args, **kwargs):
        super(CrispyUserProfileForm, self).__init__(request, *args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-profile'
        self.helper.form_method = 'post'
        self.helper.form_tag = True

        self.helper.layout = Layout(
                Field('first_name', label='', placeholder="First Name"),
                Field('last_name', label='', placeholder="Last Name"),
                Field('address', label='', placeholder="Address"),
                Field('city', label='', placeholder="City"),
                Field('state', label='', placeholder="State"),
                Field('zipcode', label='', placeholder="Zip"),
                Field('favorite_color', label='', placeholder="Favorite Color"),
                Submit('submit', "Update", css_class='btn-large')
        )


class CrispyUserRegistrationForm(UserRegistrationForm):

    def __init__(self, request=None, *args, **kwargs):
        super(CrispyUserRegistrationForm, self).__init__(request, *args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-register'
        self.helper.form_method = 'post'
        self.helper.form_tag = True

        self.helper.layout = Layout(
                Field('first_name', label='', placeholder="First Name"),
                Field('last_name', label='', placeholder="Last Name"),
                Field('email', label='', placeholder="Email"),
                Field('password1', label='', placeholder="Password"),
                Field('password2', label='', placeholder="Confirm Password"),
                Field('address', label='', placeholder="Address"),
                Field('city', label='', placeholder="City"),
                Field('state', label='', placeholder="State"),
                Field('zipcode', label='', placeholder="Zip"),
                Field('favorite_color', label='', placeholder="Favorite Color"),
                Submit('submit', "Register", css_class='btn-large')
        )
