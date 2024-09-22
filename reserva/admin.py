from django.contrib import admin
from .models import Cliente, Pago, Reserva, Habitacion, Personal

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Pago)
admin.site.register(Reserva)
admin.site.register(Habitacion)
admin.site.register(Personal)

