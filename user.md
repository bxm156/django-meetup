---
published: !<tag:yaml.org,2002:js/undefined> ""
layout: index

---

### Extending the User Model
Django provides a User model and Authentication framework with attributes and methods to help easliy integrate user authetnication into Django websites. For some developers, this is sufficient, but most find they need to store more information about their users.

There are several approaches that can be used to extend the functionality of the Django User Model

1. get_profile()
2. Proxy Objects
3. Subclassing

#### get_profile()
get_profile() has been the standard way of extending the User model in pre-1.5 Django. A second model is created with a 1-1 relationship to the Django User model. This new model can have any custom fields and methods defined, but results in extra SQL queries being performed in order to retrive the user's data.

### Subclassing
Subclassing has been a highly requested feature that was finally implemented in Django 1.5. At first glance, this may have seemed like the most obvious solution, so why did Django developers wait till 1.5?

> I’d wager that probably 90% or more of the things people say they want to do with subclasses could be better accomplished by instead defining a related model and linking it back with a unique foreign key.

_- James Bennett - [About Model Subclassing](http://www.b-list.org/weblog/2007/feb/20/about-model-subclassing/)_

James Bennet is arguing for using get_profile(), and for most cases, that is probably sufficiet. However if you want to use something other than a simple username/password you may find that you need more fields.

> Going back to the User example, there are authentication schemes which require a significantly different set of information than what the built-in User model stores; Django does its best to work around that by letting you define custom authentication backends to handle those schemes, but there are going to be systems out there which absolutely require fields the built-in User model doesn’t have, and storing additional authentication info in a related model would break encapsulation at the OO level. Subclassing User and changing the field definitions to suit is a far better solution in those particular cases.

_- James Bennett - [About Model Subclassing](http://www.b-list.org/weblog/2007/feb/20/about-model-subclassing/)_
