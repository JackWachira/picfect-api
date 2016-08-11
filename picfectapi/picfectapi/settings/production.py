"""
Production specific settings for picfect api.
"""

from .base import *
import dj_database_url
import os


DEBUG = True

DATABASES = {
    'default': dj_database_url.config()
}

MEDIA_ROOT = os.path.abspath('media')
MEDIA_URL = '/media/'
