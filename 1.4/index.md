---
published: true
layout: index

---

### Django 1.4
#### User Profile Model (One-to-One Relationship)

In Django 1.4, you could define a model that that linked to the Django User Model via a One-To-One relationship.

#####accounts/models.py
```python
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    url = models.URLField(blank=True)
```
In order for Django to know use the model as the profile, you need to define it in your settings.py

#####settings.py
```python
AUTH_PROFILE_MODULE = "accounts.UserProfile"
```

The profile model can be accessed by calling ```.get_profile()``` on the User model

#####accounts/views.py
```python
@login_required
def view_page(request):
    user_profile = request.user.get_profile()
```

###Drawbacks
* 2 Database queries
* Requires a new table
* Username is limited to 30 characters
* Its up to you to create the model when the User is created. What happens if its missing?

