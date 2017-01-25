#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Niko Skoularikis'
SITENAME = 'Real Data Talk'
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

# uncomment to bring back resume

#LINKS = (
#    ('Resume', 'https://res.cloudinary.com/dlpclqzwk/image/upload/v1485353466/20170124_Software_Engineer_lvzwbe.pdf'),
#)

# Social widget

ICONS = [
    ('github', 'https://github.com/niko79542'),
    ('linkedin', 'https://www.linkedin.com/in/nikos1'),
    ('home', 'http://www.nikoskoularikis.com/#/portfolio'),
]

DEFAULT_PAGINATION = 5

# USE THEME

THEME = "/home/niko/Documents/blog_extra/pelican-themes/pelican-alchemy/alchemy/"
THEME_COLOR = 'blue'
SITEIMAGE = 'https://res.cloudinary.com/dlpclqzwk/image/upload/v1485353473/Selection_024_ybw4f6.png'
SITESUBTITLE = 'A Data Science Learning Experience by Niko Skoularikis'

HIDE_AUTHORS = True


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb.markup']
