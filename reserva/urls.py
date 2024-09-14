from django.urls import path

from reserva.views import index, catalogo_premium, catalogo_turista, reserva

urlpatterns = [
    path('', index, name='index'),
    path('catalogo_premium/', catalogo_premium, name='catalogo_premium'),
    path('catalogo_turista/', catalogo_turista, name='catalogo_turista'),
    path('reserva/', reserva, name='reserva'),
    ]