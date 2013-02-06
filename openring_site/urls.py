#!/usr/bin/env python
# -*- coding: ISO-8859-1 -*-

# python/django imports
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

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

                       # Django comments
                       url(r'^comments/', include('django.contrib.comments.urls')),

                       # Tiny MCE editor
                       url(r'^tinymce/', include('tinymce.urls')),

                       # Django zinnia for blogging
                       url(r'^blog/', include('zinnia.urls')),


                       # Django cms
                       url(r'^', include('cms.urls')),
                       )


# serving media root with django static file
if settings.DEBUG:
    urlpatterns = patterns('',
                           url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
                               {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
                           url(r'', include('django.contrib.staticfiles.urls')),
                           ) + urlpatterns
