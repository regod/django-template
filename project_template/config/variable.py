#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
DJANGO_ROOT = os.path.dirname(os.path.dirname(__file__))

'''
_variable = {
    'debug'  : '',
    'test'   : '',
    'product': '',
}
'''

_static_root = {
    'debug'  : DJANGO_ROOT+'/webroot/static/',
    'test'   : DJANGO_ROOT+'/webroot/static/',
    'product': '',
}
_static_url = {
    'debug'  : '/static/',
    'test'   : '/static/',
    'product': '',
}
_media_root = {
    'debug'  : DJANGO_ROOT+'/webroot/media/',
    'test'   : DJANGO_ROOT+'/webroot/media/',
    'product': '',
}
_media_url = {
    'debug'  : 'http://localhost:8000/media/',
    'test'   : '/media/',
    'product': '',
}

