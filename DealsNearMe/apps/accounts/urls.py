from django.conf.urls import patterns

urlpatterns = patterns('DealsNearMe.apps.accounts.views',
    (r'^register/$', 'registration')
)
