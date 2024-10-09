from django.db import models

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

class Contrato(models.Model):
        SERVICIO_CHOICES = [
        ('agua', 'Agua'),
        ('luz', 'Luz'),
        ('gas', 'Gas'),
        ('telefonia', 'Telefonía'),
        ('internet', 'Internet'),
        ]

        PLAZOS_CHOICES = [
        ('mensual', 'Mensual'),
        ('trimestral', 'Trimestral'),
        ('anual', 'Anual'),
        ]

        servicio = models.CharField(max_length=50, choices=SERVICIO_CHOICES)
        fecha = models.DateField()
        nombres = models.CharField(max_length=100)
        apellidos = models.CharField(max_length=100)
        cedula = models.CharField(max_length=20)
        direccion = models.CharField(max_length=255)
        detalles = models.TextField(blank=True)  # No es obligatorio
        obligaciones = models.TextField(blank=True)  # No es obligatorio
        duracion = models.PositiveIntegerField()  # Duración en meses
        fecha_plazo = models.DateField()
        precio = models.DecimalField(max_digits=10, decimal_places=2)
        confidencialidad = models.BooleanField()

        def __str__(self):
                return f"Contrato de {self.nombres} {self.apellidos} para {self.servicio}"

