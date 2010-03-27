import os 
import settings
from django.conf.urls.defaults import *
from django.contrib import admin
from django.views.generic.simple import redirect_to

from bitrepo.urls import namespaced as test_urls

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', redirect_to, {'url': '/bt/'}),
    url(r'^bt/', test_urls),
    url(r'^admin/', admin.site.urls),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^jsi18n/(?P<packages>\S+?)/$', 
      'django.views.i18n.javascript_catalog'),
    url(r'^jsi18n/$', 'django.views.i18n.javascript_catalog'),
    url(r'^rosetta/', include('rosetta.urls')),

    # Media serving
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
     {'document_root': settings.MEDIA_ROOT,
     'show_indexes': True},
     name='media'), 
    )
