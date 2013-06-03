#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#'BACKEND': 'redis_cache.RedisCache',
#'LOCATION': '127.0.0.1:6379',
#'OPTIONS': {
#    'DB': 1,
#},

_cache = {
    'debug': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    },
    'test': {
        #'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        #'LOCATION': '',
    },
    'prepub': {
        #'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        #'LOCATION': '',
    },
    'product': {
        #'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        #'LOCATION': '',
        #'TIMEOUT': 864000, # 3600 x 24 x 10
    },
}
