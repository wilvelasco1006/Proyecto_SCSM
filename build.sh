#!/usr/bin/env bash

# Instala dependencias completas para WeasyPrint
apt-get update
apt-get install -y build-essential python3-dev python3-pip python3-setuptools python3-wheel python3-cffi libcairo2 libpango-1.0-0 libpangocairo-1.0-0 libgdk-pixbuf2.0-0 libffi-dev shared-mime-info fonts-liberation fontconfig

# Crear y configurar directorios temporales para WeasyPrint
mkdir -p /tmp/weasyprint
chmod 777 /tmp/weasyprint

# Configurar variables de entorno para WeasyPrint
export WEASYPRINT_CACHE=/tmp/weasyprint

# Instala dependencias de Python
pip install -r requirements.txt

# Asegurar que WeasyPrint está instalado con la versión correcta
pip install weasyprint --upgrade

# Aplica migraciones a la base de datos
python manage.py migrate


# Recoge archivos estáticos
python manage.py collectstatic --noinput
