from django.contrib import admin # admin.py

# Register your models here.
from .models import Proveedor, Cafe
# añadimos el proveedor y el cafe al admin para visulizarlo
admin.site.register(Proveedor)
admin.site.register(Cafe)
