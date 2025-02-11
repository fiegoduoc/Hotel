# Generated by Django 5.1 on 2024-09-18 20:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('id_administrador', models.AutoField(primary_key=True, serialize=False)),
                ('rut_administrador', models.IntegerField(error_messages={'unique': 'El rut ya existe'}, help_text='Ingrese su rut', unique=True, verbose_name='Rut')),
                ('nombre', models.CharField(help_text='Ingrese su nombre', max_length=50, verbose_name='Nombre')),
                ('apellido', models.CharField(help_text='Ingrese su apellido', max_length=50, verbose_name='Apellido')),
                ('email', models.EmailField(help_text='Ingrese su email', max_length=50, verbose_name='Email')),
                ('telefono', models.IntegerField(help_text='Ingrese su telefono', verbose_name='Telefono')),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id_cliente', models.AutoField(primary_key=True, serialize=False, verbose_name='ID Cliente')),
                ('rut_pasaporte', models.IntegerField(error_messages={'unique': 'El rut o pasaporte ya existe'}, help_text='Ingrese su rut o pasaporte', unique=True, verbose_name='Rut o Pasaporte')),
                ('nombre', models.CharField(help_text='Ingrese su nombre', max_length=50, verbose_name='Nombre')),
                ('apellido', models.CharField(help_text='Ingrese su apellido', max_length=50, verbose_name='Apellido')),
                ('fecha_nacimiento', models.DateField(help_text='Ingrese su fecha de nacimiento', verbose_name='Fecha de Nacimiento')),
                ('email', models.EmailField(help_text='Ingrese su email', max_length=50, verbose_name='Email')),
                ('telefono', models.IntegerField(help_text='Ingrese su telefono', verbose_name='Telefono')),
                ('direccion', models.CharField(help_text='Ingrese su direccion', max_length=50, verbose_name='Direccion')),
                ('ciudad', models.CharField(help_text='Ingrese su ciudad', max_length=50, verbose_name='Ciudad')),
                ('pais', models.CharField(help_text='Ingrese su pais', max_length=50, verbose_name='Pais')),
            ],
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id_pago', models.AutoField(primary_key=True, serialize=False)),
                ('monto', models.IntegerField(help_text='Ingrese el monto', verbose_name='Monto')),
                ('fecha_pago', models.DateField(help_text='Ingrese la fecha de pago', verbose_name='Fecha de Pago')),
                ('metodo_pago', models.CharField(help_text='Ingrese el metodo de pago', max_length=50, verbose_name='Metodo de Pago')),
                ('id_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reserva.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('id_personal', models.AutoField(primary_key=True, serialize=False)),
                ('rut_personal', models.IntegerField(error_messages={'unique': 'El rut ya existe'}, help_text='Ingrese su rut', unique=True, verbose_name='Rut')),
                ('nombre', models.CharField(help_text='Ingrese su nombre', max_length=50, verbose_name='Nombre')),
                ('apellido', models.CharField(help_text='Ingrese su apellido', max_length=50, verbose_name='Apellido')),
                ('email', models.EmailField(error_messages={'unique': 'El email ya existe'}, help_text='Ingrese su email', max_length=50, unique=True, verbose_name='Email')),
                ('telefono', models.IntegerField(help_text='Ingrese su telefono', verbose_name='Telefono')),
                ('puesto', models.CharField(help_text='Ingrese su puesto', max_length=50, verbose_name='Puesto')),
                ('id_administrador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reserva.administrador')),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id_reserva', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_reserva', models.DateField(auto_now=True, verbose_name='Fecha de Reserva')),
                ('fecha_llegada', models.DateField(help_text='Ingrese la fecha de llegada', verbose_name='Fecha de Llegada')),
                ('fecha_salida', models.DateField(help_text='Ingrese la fecha de salida', verbose_name='Fecha de Salida')),
                ('cantidad_adultos', models.IntegerField(help_text='Ingrese la cantidad de adultos', verbose_name='Cantidad de Adultos')),
                ('cantidad_ninos', models.IntegerField(help_text='Ingrese la cantidad de ninos', verbose_name='Cantidad de Ninos')),
                ('mascotas', models.BooleanField(help_text='Seleccione si trae mascotas', verbose_name='Mascotas')),
                ('id_pago', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reserva.pago')),
            ],
        ),
        migrations.CreateModel(
            name='Habitacion',
            fields=[
                ('id_habitacion', models.AutoField(primary_key=True, serialize=False)),
                ('numero_habitacion', models.IntegerField(error_messages={'unique': 'El numero de habitacion ya existe'}, help_text='Ingrese el numero de habitacion', unique=True, verbose_name='Numero de Habitacion')),
                ('tipo_habitacion', models.CharField(help_text='Ingrese el tipo de habitacion', max_length=50, verbose_name='Tipo de Habitacion')),
                ('precio', models.IntegerField(help_text='Ingrese el precio', verbose_name='Precio')),
                ('estado', models.CharField(help_text='Ingrese el estado', max_length=50, verbose_name='Estado')),
                ('disponible', models.BooleanField(help_text='Seleccione si esta disponible', verbose_name='Disponible')),
                ('tamano', models.CharField(help_text='Ingrese el tamano', max_length=50, verbose_name='Tamano')),
                ('descripcion', models.CharField(help_text='Ingrese la descripcion', max_length=50, verbose_name='Descripcion')),
                ('id_personal', models.ManyToManyField(to='reserva.personal')),
                ('id_reserva', models.ManyToManyField(to='reserva.reserva')),
            ],
        ),
    ]
