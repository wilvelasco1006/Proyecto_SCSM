"""
WSGI config for ProyectoSCSM project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# Establece la variable de entorno para la configuración de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProyectoSCSM.settings')


# Obtiene la aplicación WSGI que será utilizada por el servidor
application = get_wsgi_application()
