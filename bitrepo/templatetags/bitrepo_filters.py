#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Created by Andre Anjos <andre.dos.anjos@cern.ch>
# Sat 27 Mar 08:43:34 2010 

"""Filters for bitrepo
"""

from django import template
register = template.Library()
 
@register.filter("special_pagination")
def special_pagination(paginator):
  around = 3 # number of pages around the current one to show
  pages = range(paginator.number - around, paginator.number + around + 1) 
  pages = [k for k in pages if k > 0 and k <= paginator.paginator.num_pages]
  if pages[0] > 1: 
    if pages[0] > 2: pages.insert(0, False)
    pages.insert(0, 1)
  if pages[-1] < paginator.paginator.num_pages:
    if pages[-1] < (paginator.paginator.num_pages - 1): pages.append(False)
    pages.append(paginator.paginator.num_pages)
  return pages

