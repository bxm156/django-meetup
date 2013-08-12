from django.conf.urls import patterns
from DealsNearMe.apps.login.forms import CrispyAuthenticationForm

urlpatterns = patterns('',
        (r'^$', 'django.contrib.auth.views.login', {'template_name': 'login.djhtml', 'authentication_form': CrispyAuthenticationForm})
)
