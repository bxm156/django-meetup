---
published: true
layout: index
---

### Crispy Forms
Quickly redner forms in Django with HTML and CSRF built in. It includes layout options and Bootstrap integration.

[https://github.com/maraujop/django-crispy-forms](https://github.com/maraujop/django-crispy-forms)

Docs: [http://django-crispy-forms.rtfd.org/](http://django-crispy-forms.rtfd.org/)

Boostrap specific information: [http://django-crispy-forms.readthedocs.org/en/latest/layouts.html#bootstrap-layout-objects](http://django-crispy-forms.readthedocs.org/en/latest/layouts.html#bootstrap-layout-objects)

#### Insallation

```bash
pip install django-crispy-forms
```

##### settings.py
```python
INSTALLED_APPS = (
    # Other Apps
    'crispy_forms',
    # Other Apps
)
```

##### Usage
```python
from crispy_forms.layout import Submit, Layout, Field
from crispy_forms.helper import FormHelper

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
                Field('username', label='', placeholder="Username"),
                Field('password1', label='', placeholder="Password"),
                Field('password2', label='', placeholder="Confirm Password"),
                Field('address', label='', placeholder="Address"),
                Field('city', label='', placeholder="City"),
                Field('state', label='', placeholder="State"),
                Field('zipcode', label='', placeholder="Zip"),
                Field('favorite_color', label='', placeholder="Favorite Color"),
                Submit('submit', "Register", css_class='btn-large')
        )
```
{% raw %}
To render the form in a Django Template, add the `{% load crispy_forms_tags %}` to your template and use the `crispy` tag to render the form. For example: 

```html
{% load crispy_forms_tags %}
{% crispy form %}
```
{% endraw %}

