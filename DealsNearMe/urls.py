from django.conf.urls import patterns, include, url

import DealsNearMe.apps.accounts.urls
import DealsNearMe.apps.pages.urls

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^account/', include(DealsNearMe.apps.accounts.urls)),
    url(r'', include(DealsNearMe.apps.pages.urls)),
    # Examples:
    # url(r'^$', 'DealsNearMe.views.home', name='home'),
    # url(r'^DealsNearMe/', include('DealsNearMe.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
