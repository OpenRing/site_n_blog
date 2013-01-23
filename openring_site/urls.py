#!/usr/bin/env python
# -*- coding: ISO-8859-1 -*-

# python/django imports
from django.conf.urls import patterns, include, url
from django.contrib import admin

# Required for django admin panel
admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'openring_site.views.home', name='home'),
                       # url(r'^openring_site/', include('openring_site.foo.urls')),

                       # Django docs
                       url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

                       # Django admin
                       url(r'^admin/', include(admin.site.urls)),

                       # Django cms
                       url(r'^', include('cms.urls')),
                       )
