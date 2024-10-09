from django import forms
from django.contrib import admin
from .models import Usuario, Contrato

# Vista Admin para Usuario
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ["id", "correo", "nombre", "apellido", "clave", "rol"] 

# Formulario para el modelo Contrato
class ContratoForm(forms.ModelForm):
    class Meta:
        model = Contrato
        fields = ['servicio', 'fecha', 'nombres', 'apellidos', 'cedula', 'direccion', 'detalles', 'obligaciones', 'duracion', 'fecha_plazo', 'precio', 'confidencialidad']

# Vista Admin para Contrato
class ContratoAdmin(admin.ModelAdmin):
    form = ContratoForm  
    list_display = ['servicio', 'fecha', 'nombres', 'apellidos', 'cedula', 'direccion', 'duracion', 'precio',]

# Registrar modelos en el Admin
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Contrato, ContratoAdmin) 
