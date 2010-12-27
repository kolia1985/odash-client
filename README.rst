oDash client
============

`oDash client` is a client for send log messages and 500 errors to oDash.

Installation
------------

Install all necessary packages with::

 - Add 'odashclient' to INSTALLED_APPS.

 - Add settings options to local_settings.py:
     ODASH_REMOTE_URL = ['http://odash.odeskps.com/dashboard/store/', ]
     ODASH_KEY = '0123456789abcde'
     ODASH_PROJECT_NAME = 'slug of project name'
     ODASH_SITE_NAME = 'slug of site name'

 - For send log message to oDash use odashclient.handlers.OdashHandler

