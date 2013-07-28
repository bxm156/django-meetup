from django.conf.urls import patterns

urlpatterns = patterns('DealsNearMe.apps.login.views',
    (r'^$', 'login')
)
