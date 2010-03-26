#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Created by Andre Anjos <andre.dos.anjos@cern.ch>
# Sex 05 Mar 2010 11:48:41 CET 

"""Creates repositories for the inital tests.
"""

from django.core.management import setup_environ
import settings
setup_environ(settings)

# This bit will create the superuser
from django.contrib.auth.models import User
name = 'admin'

if User.objects.filter(username=name):
  for k in User.objects.filter(username=name):
    print 'Deleting user "%s"' % k.username
    k.delete()

admin = User()
admin.username = name
admin.first_name = name.capitalize()
admin.last_name = name.capitalize() + 'ston'
admin.email = '%s@example.com' % name
admin.is_staff = True
admin.is_active = True
admin.is_superuser = True
admin.set_password(admin.username)
admin.save()
print 'Created user "%s" with password "%s"' % (name, name)
