import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

from django.core.wsgi import get_wsgi_application
from django.core.management import call_command

try:
    call_command("migrate", interactive=False, verbosity=0)
except Exception:
    pass

application = get_wsgi_application()