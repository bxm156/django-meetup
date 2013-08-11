---
published: true
layout: index
---

### Django 1.4
#### Creating the User Profile Model

Its up to you how you want to create the User Profile Model. Most websites create it in a form during the registration process, while others may opt to use the Django Signals system.

#####Forms (accounts/forms.py)
```python
class UserRegistrationForm(UserCreationForm):
    address = forms.CharField(max_length=255, label='')
    city = forms.CharField(max_length=255, label='')
    state = USStateField(widget=USStateSelect, label='')
    zipcode = USZipCodeField(label='')
    favorite_color = forms.CharField(max_length=255, label='')

    class Meta(UserCreationForm.Meta):
        fields = ('username', 'first_name', 'last_name',)

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
            zipcode=self.cleaned_data['zipcode'],
            favorite_color=self.cleaned_data['favorite_color'],
            latitude=lat,
            longitude=lng,
        )
        user_profile.save()
```

####Signals
```python
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Define User Profile model here

def user_post_save(sender, instance, created, **kwargs):
    if created is True:
        profile = UserProfile()
        profile.user = user
        profile.save()
post_save.connect(user_post_save, sender=User)
```
