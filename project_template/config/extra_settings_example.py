#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
DJANGO_ROOT = os.path.dirname(os.path.dirname(__file__))

DATABASES = {
    'default' : {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
        'TEST_CHARSET': 'utf8',
        'TEST_COLLATION': 'utf8_general_ci',
    }
}
CACHES = {
    'default': {
        'BACKEND': 'johnny.backends.redis.RedisCache',
        'LOCATION': '127.0.0.1:6379',
        'OPTIONS': {
            'DB': 1,
        },
        'JOHNNY_CACHE': True,
    }
}
MEDIA_ROOT = DJANGO_ROOT+'/webroot/media/'
MEDIA_URL = '/media/'
STATIC_ROOT = DJANGO_ROOT+'/webroot/static/'
STATIC_URL = '/static/'

