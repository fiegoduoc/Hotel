from django.urls import path

from reserva.views import index, catalogo_premium, catalogo_turista, reserva, signup, signin, disponibilidad, pago, translate, comprobante

urlpatterns = [
    path('', index, name='index'),
    path('catalogo_premium/', catalogo_premium, name='catalogo_premium'),
    path('catalogo_turista/', catalogo_turista, name='catalogo_turista'),
    path('reserva/', reserva, name='reserva'),
    path('signup/', signup, name='signup'),
    path('signin', signin, name='signin'),
    path('disponibilidad/', disponibilidad, name='disponibilidad'),
    path('pago/', pago, name='pago'),
    path('translate/', translate, name='translate'),
    path('comprobante/', comprobante, name='comprobante')
    ]