#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
DJANGO_ROOT = os.path.dirname(os.path.dirname(__file__))

_logging = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
   'formatters': {
        'verbose': {
            'format': '%(asctime).19s [%(levelname)s] %(module)s.%(funcName)s %(filename)s:%(lineno)d: %(message)s'
        },
        'info':{
            'format': '%(asctime).19s [%(levelname)s] %(filename)s:%(lineno)d: %(message)s'
        },
        'profiler':{
            'format':"[%(asctime).19s] %(message)s"
        },
        'sql': {
            'format': '%(asctime).19s %(message)s',
        },
    },
    'handlers': {
        'console':{
            'class':'logging.StreamHandler',
            'level':'DEBUG',
            'formatter': 'verbose'
        },
        'sql': {
            'class': 'logging.handlers.WatchedFileHandler',
            'level':'DEBUG',
            'filename': DJANGO_ROOT + '/logs/sql.log',
            'formatter': 'sql',
        },
        'info': {
            'class': 'logging.handlers.WatchedFileHandler',
            'level':'INFO',
            'filename': DJANGO_ROOT + '/logs/info.log',
            'formatter': 'info',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django.db.backends': {
            'handlers': ['sql'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'debug': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'info': {
            'handlers': ['info'],
            'level': 'INFO',
            'propagate': True,
       },
    }
}

