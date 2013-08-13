---
layout: index
published: true
---

### Django 1.5
#### Custom User Profile
#####accounts/models.py
```python
from django.contrib.auth.models import AbstractBaseUser

class User(AbstractBaseUser):
    email = models.EmailField(max_length=254, unique=True, db_index=True)
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = USStateField()
    zipcode = models.CharField(max_length=15)
    favorite_color = models.CharField(max_length=255)
    latitude = models.IntegerField()
    longitude = models.IntegerField()
    latitude = models.IntegerField(null=True)
    longitude = models.IntegerField(null=True)
 
    USERNAME_FIELD = 'email'
 
    @property
    def username(self):
         return self.email
```

#####accounts/auth.py
```python
from django.contrib.auth import get_user_model

class CustomAuth(object):

    def authenticate(self, username=None, password=None):
        try:
            user = get_user_model().objects.get(email=username)
            if user.check_password(password):
                return user
        except get_user_model().DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            user = get_user_model().objects.get(pk=user_id)
            if user.is_active:
                return user
            return None
        except get_user_model().DoesNotExist:
            return None
```

#####settings.py
```python
AUTH_USER_MODEL = 'accounts.User'
AUTHENTICATION_BACKENDS = ('DealsNearMe.apps.accounts.auth.CustomAuth',)
```