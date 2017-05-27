#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import numpy as np

AUTHOR = 'Sylvia Moulin'
SITENAME = 'Sylvia Moulin'
SITEURL = ''

PATH = 'content'
PLUGIN_PATHS = ['pelican-plugins']

TIMEZONE = 'Europe/Paris'
THEME = 'themes/pure'

DEFAULT_LANG = 'fr'

# Feed generation is usually not desired when developing
# FEED_ALL_ATOM = None
# CATEGORY_FEED_ATOM = None
# TRANSLATION_FEED_ATOM = None
# AUTHOR_FEED_ATOM = None
# AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

## Paths

USE_FOLDER_AS_CATEGORY = False

# article data gets written to article directory
STATIC_PATHS = [
    'images', 
    'extra/favicon.ico',
	'category/architecture',  
	'category/identite-visuelle',
	'category/danse',
	'category/decouverte'
]


# ARTICLE_SAVE_AS = 'category/{category}/{slug}.html'
# ARTICLE_URL = 'category/{category}/{slug}.html'

USE_FOLDER_AS_CATEGORY= True

# STATIC_SAVE_AS = '/category/{category}/'  #this is the default anyway
STATIC_EXCLUDE_SOURCES=True

# if date not specified, Pelican will use file’s “mtime” timestamp
DEFAULT_DATE = 'fs' 

# Markup
TYPOGRIFY = True

##############
# Dev option
##############

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# erase output content every time
DELETE_OUTPUT_DIRECTORY = True


