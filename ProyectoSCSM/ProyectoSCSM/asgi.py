"""
ASGI config for ProyectoSCSM project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

# Establece la variable de entorno para la configuración de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProyectoSCSM.settings')

# Obtiene la aplicación ASGI que será utilizada por el servidor
application = get_asgi_application()
