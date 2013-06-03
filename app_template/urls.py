#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from django.conf.urls import patterns, include, url

urlpatterns = patterns('apps.{{ app_name }}.views',
    url(r'test/', 'test', name='test'),
)
