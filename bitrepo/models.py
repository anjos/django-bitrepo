#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Created by Andre Anjos <andre.dos.anjos@cern.ch>
# Sex 26 Mar 2010 11:59:46 CET 

"""Models for our DB entries
"""

import os, datetime, hashlib
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ugettext
from django.conf import settings
from django.contrib.auth.models import User

def upload_path(object, original):
  """Tells the FileField how to choose a name for this file."""
  if hasattr(object, 'name'):
    d = hashlib.sha1(object.name).hexdigest()[:8]
    date = object.date
  else:
    d = hashlib.sha1(object.movie.name).hexdigest()[:8]
    date = object.movie.date
  f = hashlib.sha1(original).hexdigest()[:8]
  return os.path.join('packages', date.strftime('%Y/%m'), d, f)

class Package(models.Model):
  """Describes a Downloadable package."""

  user = models.ForeignKey(User, null=False)

  name = models.CharField(_(u'Name'), max_length=255, 
    help_text=_(u'Set the name of the package in this entry.'), 
    null=False, blank=False, unique=True)

  date = models.DateTimeField(_('Creation date'), 
      auto_now_add=True, editable=False, null=False, blank=False)

  torrent = models.FileField(_('Torrent'), upload_to=upload_path,
      help_text=_('Specify here the torrent file that should be uploaded.'),
      null=False, blank=False)

  def __unicode__(self):
    return ugettext(u"Package '%(name)s'" % {'name':self.name})

  # make it translatable
  class Meta:
    verbose_name = _('package')
    verbose_name_plural = _('packages')

class Movie(Package):
  """Describes a movie package."""

  year = models.PositiveIntegerField(_(u'Year'), 
      default=datetime.date.today().year,
      help_text=_(u'Set here the year in which the movie was released.'),
      null=False, blank=False)

  link = models.URLField(_(u'Link'),
      help_text=_(u'Set here an optional URL to a website containing a description of this movie (e.g. the movie website or the IMDB page).'),
      null=True, blank=True)

  def __unicode__(self):
    return ugettext(u"Movie '%(name)s'" % {'name':self.name})

  # make it translatable
  class Meta:
    verbose_name = _('movie')
    verbose_name_plural = _('movie')

class Subtitle(models.Model):
  """This movie's subtitle track."""

  movie = models.ForeignKey(Movie)

  original = models.CharField(_('Original'), max_length='100',
      null=True, blank=True, editable=False,)

  language = models.CharField(_('Language'), max_length=6,
      help_text=_(u'Specify the language at this subtitle file.'),
      choices=settings.LANGUAGES, null=False, blank=False)

  file = models.FileField(_('Subtitle'), upload_to=upload_path,
      help_text=_('Specify here the subtitle file that should be uploaded.'),
      null=False, blank=False)

  def save(self, *args, **kwargs):
    """Saves the original filename for this subtitle"""
    self.original = self.file.name
    super(Subtitle, self).save(*args, **kwargs)

  def __unicode__(self):
    return ugettext(u"%(language)s subtitles for movie '%(name)s'" % \
        {'language': self.language, 'name': self.movie.name})

  # make it translatable
  class Meta:
    verbose_name = _('subtitle')
    verbose_name_plural = _('subtitles')
