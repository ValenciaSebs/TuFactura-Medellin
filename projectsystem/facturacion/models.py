from django.db import models

# Create your models here.
class Usuario(models.Model):
    correo = models.EmailField(max_length=254, unique = True)
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    clave = models.CharField(max_length=254)
    ROLES =(
            ('U', "Usuario"),
    )
    rol = models.CharField(max_length=1, choices=ROLES, default='U')