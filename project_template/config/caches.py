#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#'BACKEND': 'redis_cache.RedisCache',
#'LOCATION': '127.0.0.1:6379',
#'OPTIONS': {
#    'DB': 1,
#},

# django.core.cache.backends.dummy.DummyCache
# django.core.cache.backends.memcached.MemcachedCache
# django.core.cache.backends.filebased.FileBasedCache
# redis_cache.RedisCache

_cache = {
    'debug': {
        'BACKEND': 'redis_cache.RedisCache',
        'LOCATION': '127.0.0.1:6379',
        'TIMEOUT': 86400, # 3600 x 24
        'OPTIONS': {
            'DB': 1,
        },
        'JOHNNY_CACHE': True,
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
