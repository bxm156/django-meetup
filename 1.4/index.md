---
published: true
layout: index

---

### Django 1.4
#### User Profile Model

In Django 1.4, you could define a model that that linked to the Django User Model.

#####accounts/models.py
```python
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    url = models.URLField(blank=True)
```

#####settings.py
```python
AUTH_PROFILE_MODULE = "accounts.UserProfile"
````

#####accounts/views.py
```python
@login_required
def view_foo(request):
    user_profile = request.user.get_profile()
```
