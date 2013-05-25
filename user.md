### Extending the User Model

Django provides a User model and Authentication framework with attributes and methods to help easliy integrate user authetnication into Django websites. For some developers, this is sufficient, but most find they need to store more information about their users.

There are several approaches that can be used to extend the functionality of the Django User Model

1. get_profile()
2. Proxy Objects
3. Subclassing

#### get_profile()
get_profile() has been the standard way of extending the User model in pre-1.5 Django. A second model is created with a 1-1 relationship to the Django User model. This new model can have any custom fields and methods defined, but results in extra SQL queries being performed in order to retrive the user's data.



