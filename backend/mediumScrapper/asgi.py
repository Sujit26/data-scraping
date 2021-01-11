"""
ASGI config for mediumScrapper project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""
import os
import django

from django.core.asgi import get_asgi_application
# from channels.routing import get_default_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mediumScrapper.settings')

django.setup()

application = get_asgi_application()


# import os

# from channels.routing import get_default_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tabulator.settings')
# application = get_asgi_application()
