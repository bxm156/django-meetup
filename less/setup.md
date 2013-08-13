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