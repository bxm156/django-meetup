---
published: true
layout: index
---

### Setup with Django
Packages: [django-compressor](http://django-compressor.readthedocs.org/en/latest/)

http://django-compressor.readthedocs.org/en/latest/quickstart/#installation
#### pip
```bash
pip install django_compressor
```

#### settings.py
Add 'compressor' to your listed of installed applications

```python
INSTALLED_APPS = (
    # other apps
    "compressor",
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # other finders..
    'compressor.finders.CompressorFinder',
)
# LESS Compiler
COMPRESS_ENABLED = True
COMPRESS_PRECOMPILERS = (
    ('text/less', 'lessc {infile} {outfile}'),
)
```


#### With Heroku
Add the following directory to your root application path, in a folder called "bin".
[https://github.com/bxm156/django-meetup/tree/master/bin](https://github.com/bxm156/django-meetup/tree/master/bin)

Upon once your Heroku app is compiled, these scripts will:


1. Install NodeJS

2. Install LESS

3. Run collectstatic

4. Compress!