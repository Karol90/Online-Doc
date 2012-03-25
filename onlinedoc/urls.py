from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
#from bookmarks.views import *
admin.autodiscover()

urlpatterns = patterns(
    url(r'^$', index),
    # url(r'^$', 'accounts.views.index', name='home'),
    # url(r'^onlinedoc/', include('onlinedoc.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

)

include('messages.urls')