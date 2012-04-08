from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

"""
D: Zamiana mainsite na frontpage?
"""
urlpatterns = patterns('',
    # Home page
    url(r'^$', 'mainsite.views.index', name='home'),
    
    # Account
    url(r'^acc/$', 'accounts.views.acc', name='link1'),
    
    # Messages, required django-messages application
    # url(r'^messages/', include(messages.urls)),
    
    # Django documentation
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    
    # Django administration
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^index/$', 'mainsite.views.hello'),
    
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )