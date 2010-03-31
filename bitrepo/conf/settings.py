#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Created by Andre Anjos <andre.dos.anjos@cern.ch>
# Sex 26 Mar 2010 16:38:08 CET 

"""Settings for bitrepo
"""

from django.conf import settings

BITREPO_MEDIA_URL = getattr(settings, 'BITREPO_MEDIA_URL', 
    settings.MEDIA_URL + 'bitrepo/')
