from django.conf.urls import patterns

urlpatterns = patterns('DealsNearMe.apps.accounts.views',
    (r'^$', 'overview'),
    (r'^register/$', 'registration'),
    (r'^profile/$', 'edit_profile'),
    (r'^logout/$', 'logout'),
)
