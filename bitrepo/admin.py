#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Created by Andre Anjos <andre.dos.anjos@cern.ch>
# Sex 26 Mar 2010 15:56:20 CET 

"""Administration models for bitrepo
"""

from django.contrib import admin
from models import *
from django.utils.translation import ugettext_lazy as _
from bitrepo.conf import settings

class SubtitleInline(admin.StackedInline):
  model = Subtitle
  fieldsets = (
      (None, {'fields': ('language', 'file',)}),
    )
  extra = 2
    
class MovieAdmin(admin.ModelAdmin):
  list_display = ('name', 'year', 'user', 'date', 'link',)
  list_filter = ['name', 'year', 'user', 'date',]
  list_per_page = 10
  ordering = ['-date']
  search_fields = ['name', 'year', 'user']
  #date_hierarchy = 'date'
  inlines = [
      SubtitleInline,
      ]

  #class Media:
  #  js = (
  #    "http://ajax.googleapis.com/ajax/libs/jquery/1.3.2/jquery.min.js",
  #    settings.BITREPO_MEDIA_URL + "js/add_tabular_inline.js",
  #  )

admin.site.register(Movie, MovieAdmin)


