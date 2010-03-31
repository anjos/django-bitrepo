#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Created by Andre Anjos <andre.dos.anjos@cern.ch>
# Qua 31 Mar 2010 16:19:14 CEST 

"""Mail functions for bitrepo
"""
import datetime
from django.template import loader
from django.contrib.auth.models import Group
from django.contrib.sites.models import Site
from django.utils.translation import ugettext_lazy as _
from django.core.mail import send_mail
from django.conf import settings

#bitrepo stuff
from models import Movie

def mail_digest(days, group, message_template='bitrepo/digest.txt'):

  # get group
  g = Group.objects.get(name=group)

  # check if the group has users
  users = g.user_set.all()
  if not users: raise RuntimeError, 'No users found in group %s' % group 
  
  # checks something new has been posted
  start = datetime.datetime.now() - datetime.timedelta(days=days)
  objects = Movie.objects.filter(date__gte=start)
  if not objects: raise RuntimeError, 'No new movies found'

  # if you get to this point, you have all, just pack the mail and send 
  sender = settings.DEFAULT_FROM_EMAIL

  subject = _(u'[%(site)s] Movie digest - %(movies)d movies in the last %(days)d days' % \
      { 'movies': len(objects),
        'site': Site.objects.get_current().domain,
        'days': days,
      }
    )

  message = loader.render_to_string(message_template, 
      {
        'objects': objects.order_by('date'),
        'site': Site.objects.get_current(),
        'days': days,
      }
    ) 

  to = [u'%s <%s>' % (k.get_full_name(), k.email) for k in users]
  send_mail(subject=subject, message=message, from_email=sender, 
      recipient_list=to)
