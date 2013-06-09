from django.conf.urls import patterns

urlpatterns = patterns('DealsNearMe.apps.pages.views',
    (r'^$', 'homepage')
)
