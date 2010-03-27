#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Created by Andre Anjos <andre.dos.anjos@cern.ch>
# Seg 14 Set 2009 14:42:06 CEST 

"""Installation instructions for django-multilingual
"""

from setuptools import setup, find_packages

setup(

    name = 'django-bitrepo',
    version = '0.1',
    packages = find_packages(),

    # we also need all translation files and templates
    package_data = {
      'bitrepo': [
        'templates/bitrepo/*.html',
        'media/js/*.js',
        'media/img/svg/*.svg',
        'media/img/png/*/*.png',
        ],
      },

    entry_points = {
      'console_scripts': [
        ],
      },

    zip_safe=False,

    install_requires = [
      'Django>=1.1',
      'docutils',
      ],

    # metadata for upload to PyPI
    author = 'André Anjos',
    author_email = "andre.dos.anjos@gmail.com",
    description = 'Torrent repository extension for Django',
    license = "GPL v2 or superior",
    keywords = "django bit torrent",
    url = 'http://andreanjos.org/project/django-bitrepo/',
)
