import logging
import sys

class OdashHandler(logging.Handler):
    def emit(self, record):
        from odashclient.models import get_client

        # Avoid typical config issues by overriding loggers behavior
        if record.name == 'odashclient.errors':
            print >> sys.stderr, "Recursive log message sent to OdashHandler"
            print >> sys.stderr, record.getMessage()
            return

        get_client().create_from_record(record)
