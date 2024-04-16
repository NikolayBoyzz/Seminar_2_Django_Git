import os

"""
WSGI config for project.

It exposes the WSGI callable as a module-level variable named ``application``.

"""


from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

application = get_wsgi_application()