#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Created by Andre Anjos <andre.dos.anjos@cern.ch>
# Sex 26 Mar 2010 17:46:37 CET 

"""Views for bitrepo.
"""

import zipfile, tempfile

from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.template import RequestContext
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.contrib.auth.decorators import login_required

from models import *

@login_required
def view_list(request, template_name='bitrepo/list.html'):
  objs = Package.objects.all().order_by('-date')
  paginator = Paginator(objs, 10)

  try:
    page = int(request.GET.get('page', '1'))
  except ValueError:
    page = 1

  try:
    objs = paginator.page(page)
  except (EmptyPage, InvalidPage):
    objs = paginator.page(paginator.num_pages)
  
  return render_to_response(template_name, 
      {
        'pages': objs,
      }, 
      context_instance=RequestContext(request))

@login_required
def view_package(request, id, template_name='bitrepo/package.html'):
  obj = Package.object.get(id=id)
  return render_to_response(template_name, 
      {
        'object': object,
      }, 
      context_instance=RequestContext(request))

def make_zip(obj):
  """Makes a zip ball out of the files attached to obj, in a standard way."""
  f = tempfile.TemporaryFile()
  zf = zipfile.ZipFile(f, 'w') 
  zf.write(obj.torrent.path, 'download.torrent')
  for sub in obj.subtitle_set.all():
    zf.write(sub.file.path, sub.original.encode('latin-1', 'ignore'))
  zf.close()
  f.seek(0)
  return f.read() #read all and return to the caller.

@login_required
def zip_package(request, id): 
  obj = Package.objects.get(id=id)
  data = make_zip(obj)
  retval = HttpResponse(data, mimetype='application/zip')
  retval['Content-Disposition'] = 'attachment; filename="%s.zip"' % obj.name
  retval['Content-Length'] = len(data)
  return retval

@login_required
def get_torrent(request, id):
  obj = Package.objects.get(id=id)
  obj.torrent.open(mode='rb')
  data = obj.torrent.read()
  retval = HttpResponse(data, mimetype='application/x-bittorrent')
  retval['Content-Disposition'] = 'attachment; filename="%s.torrent"' % obj.name
  retval['Content-Length'] = len(data)
  return retval
