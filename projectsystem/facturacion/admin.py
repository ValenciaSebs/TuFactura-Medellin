from django.contrib import admin
from .models import *

# vista Admin
class UsuarioAdmin (admin.ModelAdmin):
    list_display = ["id","correo","nombre", "apellido", "clave", "rol"] 


#Meter tabla en la base de datos
admin.site.register(Usuario, UsuarioAdmin)