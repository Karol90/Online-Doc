from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'mainsite.views.index', name='home'),
    # url(r'^onlinedoc/', include('onlinedoc.foo.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^index/$', 'mainsite.views.hello'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )

#include('messages.urls')