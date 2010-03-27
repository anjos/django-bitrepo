#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Created by Andre Anjos <andre.dos.anjos@cern.ch>
# Sex 26 Mar 2010 17:40:46 CET 

"""URLs for bitrepo
"""

from django.conf.urls.defaults import *
from bitrepo.views import *

urlpatterns = patterns('',

  url(r'^$', view_list, name='index'),
  url(r'^zip/(?P<id>\d+)/$', zip_package, name='zip'),
  url(r'^torrent/(?P<id>\d+)/$', get_torrent, name='torrent'),
  
)

namespaced = (urlpatterns, 'bitrepo', 'bitrepo')


