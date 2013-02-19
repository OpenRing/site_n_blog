# Django settings for openring_site project.

import socket
import os

HOST_NAME = ['']

# check machine by its host name and decide which values to take
if socket.gethostname() in HOST_NAME:
    from production import *
else:
    from development import *

gettext = lambda s: s

DEBUG = DEBUG
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('OpenRing', 'openring0909@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.%s' % DB_ENGINE,  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': DB_NAME,                      # Or path to database file if using sqlite3.
        'USER': DB_USER,                      # Not used with sqlite3.
        'PASSWORD': DB_PASS,                  # Not used with sqlite3.
        'HOST': DB_HOST,                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': DB_PORT,                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Path for manage.py
PROJECT_PATH = os.path.dirname(__file__)
# Project root path
PROJECT_ROOT = os.path.abspath(os.path.join(PROJECT_PATH, os.path.pardir))

# Default language
LANGUAGES = [
    ('en', 'English'),
]

# Default languge for Django cms
CMS_LANGUAGES = (
    ('en', gettext('English')),
)

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT, "media")

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
# MEDIA_URL = '/media/'
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
# NOTE: All files collected with django static finder will be located here
STATIC_ROOT = os.path.join(PROJECT_ROOT, "sitestatic")

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.abspath(os.path.join(PROJECT_ROOT, 'static')),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'n*k1z=9+b5douze=bkakk)o8$-4b$#34af@@ntdz8-qg_fld5j'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    #     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # Django cms middleware
    'cms.middleware.multilingual.MultilingualURLMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'cms.context_processors.media',
    'sekizai.context_processors.sekizai',
    'zinnia.context_processors.version',
)

ROOT_URLCONF = 'openring_site.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'openring_site.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.abspath(os.path.join(PROJECT_ROOT, 'templates')),
)

# Templates for cms
CMS_TEMPLATES = (
    ('home.html', gettext('Home Page')),
    ('contactus.html', gettext('ContactUs Page')),
)


INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.comments',

    # Django admin
    'django.contrib.admin',

    # Django admin docs
    'django.contrib.admindocs',

    # For commom template tags only
    'common_tags',

    # Django cms
    'cms',

    # Cms plugins
    'cms.plugins.text',
    'cms.plugins.picture',
    'cms.plugins.snippet',
    'cmsplugin_contact',
    # 'cmsplugin_zinnia',

    # Zinnia for Blogging
    'zinnia',

    # Tagging app
    'tagging',

    # Modified preorder tree traverser
    'mptt',

    # Helper menus for django
    'menus',

    # Database imgration tool
    'south',

    # Template blocks for extra functionality
    'sekizai',

    # Tiny mce editor
    'tinymce',
)

# For django cms and zinnia
# ZINNIA_ENTRY_BASE_MODEL = 'cmsplugin_zinnia.placeholder.EntryPlaceholder'

# Menus for django cms and zinnia
# CMSPLUGIN_ZINNIA_APP_MENUS = (
#     'cmsplugin_zinnia.menu.EntryMenu',
#     'cmsplugin_zinnia.menu.CategoryMenu',
#     'cmsplugin_zinnia.menu.TagMenu',
#     'cmsplugin_zinnia.menu.AuthorMenu'
# )

# default pagination for zinnia blog
ZINNIA_PAGINATION = 5

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'detailed': {
            'format': '%(asctime)-8s %(module)-8s line:%(lineno)-4d '
            '%(levelname)-8s %(message)s',
        },
    },
    'handlers': {
        'file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'DEBUG',
            'formatter': 'detailed',
            'filename': os.path.abspath(os.path.join(PROJECT_ROOT, "logs/openring.log")),
            'mode': 'a',
            'maxBytes': 10485760,
            'backupCount': 5,
        },
        'sentry': {
            'level': 'DEBUG',
            'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'openring': {
            'level': 'DEBUG',
            'handlers': ['console', 'sentry', 'file'],
            'propagate': False,
        },
        'django.request': {
            'level': 'ERROR',
            'handlers': ['console', 'sentry', 'file'],
            'propagate': False,
        },
    },
}

# get csc logger
import logging
LOGGER = logging.getLogger('openring')

DEFAULT_FROM_EMAIL = 'openring0909@gmail.com'

# Email settings
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'openring0909@gmail.com'
EMAIL_HOST_PASSWORD = 'OpenRing09'
EMAIL_PORT = 587
