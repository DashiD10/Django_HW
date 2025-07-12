import os
import django
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'barbershop.settings')
django.setup()

print("INSTALLED_APPS:", settings.INSTALLED_APPS)
print("django_extensions в INSTALLED_APPS:", 'django_extensions' in settings.INSTALLED_APPS)
