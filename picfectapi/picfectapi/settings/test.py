"""
Test settings for picfect api.
"""

from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(os.path.dirname(__file__), 'test.db')
    }
}
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

NOSE_ARGS = [
    '--with-coverage',
    '--cover-package=api',
]

MEDIA_ROOT = os.path.abspath('test_media')
MEDIA_URL = '/media/'
