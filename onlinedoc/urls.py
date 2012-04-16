from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.contrib import admin
from django.contrib.auth.views import login, logout
admin.autodiscover()

"""
D: Zamiana mainsite na frontpage?
"""
urlpatterns = patterns('',
    # Home page
    url(r'^$', 'mainsite.views.index', name='home'),
    
    # Account
    url(r'^acc/$', 'accounts.views.acc', name='link1'),
    url(r'^accounts/login/$', 'accounts.views.login_view', name='login'),
    url(r'^accounts/logout/$', 'accounts.views.logout', name='logout'),
    url(r'^accounts/register/$', 'accounts.views.register', name='register'),
    url(r'^accounts/profile/$', 'accounts.views.profile', name='profile'),
    # url(r'^onlinedoc/', include('onlinedoc.foo.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    
    # Django administration
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^index/$', 'mainsite.views.hello'),
    
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )