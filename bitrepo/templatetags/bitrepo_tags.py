#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Created by Andre Anjos <andre.dos.anjos@cern.ch>
# Sat 27 Mar 08:42:10 2010 

"""Tags for bitrepo.
"""

from django import template
register = template.Library()
 
@register.inclusion_tag('bitrepo/paginator.html')
def bitrepo_paginator(paginator):
  return {'paginator': paginator}

