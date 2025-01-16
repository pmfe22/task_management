import os
import sys

sys.path.insert(0, '/home/pmfeir/domains/pmfe.ir/public_html/task_management')
os.environ['DJANGO_SETTINGS_MODULE'] = 'task_management.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
