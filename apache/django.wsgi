import os,sys

sys.path.append('/var/www/')
sys.path.append('/var/www/Transparencia/')

os.environ['DJANGO_SETTINGS_MODULE'] = 'Transparencia.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
