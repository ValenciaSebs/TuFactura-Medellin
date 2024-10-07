# Generated by Django 5.1.1 on 2024-10-07 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correo', models.EmailField(max_length=254, unique=True)),
                ('cedula', models.IntegerField(max_length=15)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('clave', models.CharField(max_length=254)),
                ('rol', models.CharField(choices=[('U', 'Usuario')], default='U', max_length=1)),
            ],
        ),
    ]
