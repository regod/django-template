#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
DJANGO_ROOT = os.path.dirname(os.path.dirname(__file__))

'''
_variable = {
    'debug'  : '',
    'test'   : '',
    'prepub' : '',
    'product': '',
}
'''

_static_root = {
    'debug'  : DJANGO_ROOT+'/webroot/static/',
    'test'   : DJANGO_ROOT+'/webroot/static/',
    'prepub' : '',
    'product': '',
}
_static_url = {
    'debug'  : '/static/',
    'test'   : '/static/',
    'prepub' : '',
    'product': '',
}
_media_root = {
    'debug'  : DJANGO_ROOT+'/webroot/media/',
    'test'   : DJANGO_ROOT+'/webroot/media/',
    'prepub' : '',
    'product': '',
}
_media_url = {
    'debug'  : 'http://localhost:8000/media/',
    'test'   : '/media/',
    'prepub' : '',
    'product': '',
}

