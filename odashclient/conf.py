from django.conf import settings
from django.utils.hashcompat import md5_constructor
import socket

# Allow local testing of Sentry even if DEBUG is enabled
DEBUG = getattr(settings, 'DEBUG', False) and not getattr(settings, 'SENTRY_TESTING', False)

default_client = 'odashclient.base.OdashClient'

CLIENT = getattr(settings, 'ODASH_CLIENT', default_client)

ODASH_PROJECT_NAME = getattr(settings, 'ODASH_PROJECT_NAME', None)
ODASH_SITE_NAME = getattr(settings, 'ODASH_SITE_NAME', None)

# This should be the full URL to sentries store view
REMOTE_URL = getattr(settings, 'ODASH_REMOTE_URL', None)

if REMOTE_URL:
    if isinstance(REMOTE_URL, basestring):
        REMOTE_URL = [REMOTE_URL]
    elif not isinstance(REMOTE_URL, (list, tuple)):
        raise ValueError("ODASH_REMOTE_URL must be of type list.")

REMOTE_TIMEOUT = getattr(settings, 'ODASH_REMOTE_TIMEOUT', 5)

NAME = getattr(settings, 'ODASH_NAME', socket.gethostname())

THRASHING_TIMEOUT = getattr(settings, 'ODASH_THRASHING_TIMEOUT', 60)
THRASHING_LIMIT = getattr(settings, 'ODASH_THRASHING_LIMIT', 10)

KEY = getattr(settings, 'ODASH_KEY', md5_constructor(settings.SECRET_KEY).hexdigest())

# Extending this allow you to ignore module prefixes when we attempt to
# discover which function an error comes from (typically a view)
EXCLUDE_PATHS = getattr(settings, 'ODASH_EXCLUDE_PATHS', [])

# By default Sentry only looks at modules in INSTALLED_APPS for drilling down
# where an exception is located
INCLUDE_PATHS = getattr(settings, 'ODASH_INCLUDE_PATHS', [])
