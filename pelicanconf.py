#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Niko Skoularikis'
SITENAME = 'How to Learn Data Science'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Home', 'http://www.nikoskoularikis.com/#/portfolio'),
         ('Resume', 'https://res.cloudinary.com/dlpclqzwk/image/upload/v1483140920/20161120_Front_End_Res_op0ktw.pdf'),)

# Social widget
SOCIAL = (('Linkedin', 'https://www.linkedin.com/in/nikos1'),
          ('Github', 'https://github.com/niko79542'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb.markup']