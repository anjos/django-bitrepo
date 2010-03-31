#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Created by Andre Anjos <andre.dos.anjos@cern.ch>
# Qua 31 Mar 2010 16:55:47 CEST 

"""Mails a bitrepo digest for selected users
"""

import os, sys
if not os.environ.has_key('DJANGO_SETTINGS_MODULE'):
  os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from bitrepo.mail import mail_digest

def main():

  if len(sys.argv) != 3:
    print 'usage: %s <days> <group>' % sys.argv[0]
    sys.exit(1)
  
  try:
    mail_digest(int(sys.argv[1]), sys.argv[2])
  except Exception, e:
    print '%s, WARNING: %s' % (os.path.basename(sys.argv[0]), e)
    sys.exit(1)

  sys.exit(0)
