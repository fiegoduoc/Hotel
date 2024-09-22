from django.db import models
from django.contrib.auth.models import AbstractUser

class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True, verbose_name='ID Cliente',)
    rut_pasaporte = models.IntegerField(unique=True, null=False, blank=False,
                                        verbose_name='Rut o Pasaporte', help_text='Ingrese su rut o pasaporte',
                                        error_messages={'unique': 'El rut o pasaporte ya existe'})
    nombre = models.CharField(max_length=50, null=False, blank=False, verbose_name='Nombre',
                              help_text='Ingrese su nombre')
    apellido = models.CharField(max_length=50, null=False, blank=False, verbose_name='Apellido',
                                help_text='Ingrese su apellido')
    fecha_nacimiento = models.DateField(null=False, blank=False, verbose_name='Fecha de Nacimiento',
                                        help_text='Ingrese su fecha de nacimiento')
    telefono = models.IntegerField(null=False, blank=False, verbose_name='Telefono',
                                   help_text='Ingrese su telefono')
    direccion = models.CharField(max_length=50, null=False, blank=False, verbose_name='Direccion',
                                 help_text='Ingrese su direccion')
    ciudad = models.CharField(max_length=50, null=False, blank=False, verbose_name='Ciudad',
                              help_text='Ingrese su ciudad')
    pais = models.CharField(max_length=50, null=False, blank=False, verbose_name='Pais', help_text='Ingrese su pais')


    def __str__(self):
        return self.rut_pasaporte


class Reserva(models.Model):
    id_reserva = models.AutoField(primary_key=True)
    fecha_reserva = models.DateField(auto_now=True, null=False, blank=False, verbose_name='Fecha de Reserva')
    fecha_llegada = models.DateField(null=False, blank=False, verbose_name='Fecha de Llegada',
                                     help_text='Ingrese la fecha de llegada')
    fecha_salida = models.DateField(null=False, blank=False, verbose_name='Fecha de Salida',
                                    help_text='Ingrese la fecha de salida')
    cantidad_adultos = models.IntegerField(null=False, blank=False, verbose_name='Cantidad de Adultos',
                                           help_text='Ingrese la cantidad de adultos')
    cantidad_ninos = models.IntegerField(null=False, blank=False, verbose_name='Cantidad de Ninos',
                                         help_text='Ingrese la cantidad de ninos')
    mascotas = models.BooleanField(null=False, blank=False, verbose_name='Mascotas',
                                   help_text='Seleccione si trae mascotas')
    id_pago = models.ForeignKey('Pago', on_delete=models.CASCADE)

    def __str__(self):
        return self.id_reserva


class Habitacion(models.Model):
    id_habitacion = models.AutoField(primary_key=True)
    numero_habitacion = models.IntegerField(unique=True, null=False, blank=False,
                                            verbose_name='Numero de Habitacion',
                                            help_text='Ingrese el numero de habitacion',
                                            error_messages={'unique': 'El numero de habitacion ya existe'})
    tipo_habitacion = models.CharField(max_length=50, null=False, blank=False, verbose_name='Tipo de Habitacion',
                                       help_text='Ingrese el tipo de habitacion')
    precio = models.IntegerField(null=False, blank=False, verbose_name='Precio',
                                 help_text='Ingrese el precio')
    estado = models.CharField(max_length=50, null=False, blank=False, verbose_name='Estado',
                              help_text='Ingrese el estado')
    disponible = models.BooleanField(null=False, blank=False, verbose_name='Disponible',
                                     help_text='Seleccione si esta disponible')
    tamano = models.CharField(max_length=50, null=False, blank=False, verbose_name='Tamano',
                              help_text='Ingrese el tamano')
    descripcion = models.CharField(max_length=50, null=False, blank=False, verbose_name='Descripcion',
                                   help_text='Ingrese la descripcion')
    id_reserva = models.ManyToManyField('Reserva')
    id_personal = models.ManyToManyField('Personal')

    def __str__(self):
        return self.numero_habitacion


class Pago(models.Model):
    id_pago = models.AutoField(primary_key=True)
    monto = models.IntegerField(null=False, blank=False, verbose_name='Monto',
                                help_text='Ingrese el monto')
    fecha_pago = models.DateField(auto_now=True, null=False, blank=False, verbose_name='Fecha de Pago',
                                  help_text='Ingrese la fecha de pago')
    metodo_pago = models.CharField(max_length=50, null=False, blank=False, verbose_name='Metodo de Pago',
                                   help_text='Ingrese el metodo de pago')
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return self.id_pago


class Personal(models.Model):
    id_personal = models.AutoField(primary_key=True)
    rut_personal = models.IntegerField(unique=True, null=False, blank=False, verbose_name='Rut',
                                       help_text='Ingrese su rut', error_messages={'unique': 'El rut ya existe'})
    nombre = models.CharField(max_length=50, null=False, blank=False, verbose_name='Nombre',
                              help_text='Ingrese su nombre')
    apellido = models.CharField(max_length=50, null=False, blank=False, verbose_name='Apellido',
                                help_text='Ingrese su apellido')
    email = models.EmailField(max_length=50, null=False, blank=False, verbose_name='Email',
                              help_text='Ingrese su email', unique=True, error_messages={'unique': 'El email ya existe'})
    telefono = models.IntegerField(null=False, blank=False, verbose_name='Telefono',
                                   help_text='Ingrese su telefono')
    puesto = models.CharField(max_length=50, null=False, blank=False, verbose_name='Puesto',
                              help_text='Ingrese su puesto')
    id_administrador = models.ForeignKey('Administrador', on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Administrador(models.Model):
    id_administrador = models.AutoField(primary_key=True)
    rut_administrador = models.IntegerField(unique=True, null=False, blank=False, verbose_name='Rut',
                                            help_text='Ingrese su rut', error_messages={'unique': 'El rut ya existe'})
    nombre = models.CharField(max_length=50, null=False, blank=False, verbose_name='Nombre',
                              help_text='Ingrese su nombre')
    apellido = models.CharField(max_length=50, null=False, blank=False, verbose_name='Apellido',
                                help_text='Ingrese su apellido')
    email = models.EmailField(max_length=50, null=False, blank=False, verbose_name='Email',
                              help_text='Ingrese su email')
    telefono = models.IntegerField(null=False, blank=False, verbose_name='Telefono',
                                   help_text='Ingrese su telefono')

    def __str__(self):
        return self.nombre
