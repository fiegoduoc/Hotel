from django.urls import path

from reserva.views import index, catalogo_premium, catalogo_turista, reserva, disponibilidad, pago, \
    translate, comprobante, registro, login_user, logout_user, user_page
urlpatterns = [
    path('', index, name='index'),
    path('catalogo_premium/', catalogo_premium, name='catalogo_premium'),
    path('catalogo_turista/', catalogo_turista, name='catalogo_turista'),
    path('reserva/', reserva, name='reserva'),
    path('disponibilidad/', disponibilidad, name='disponibilidad'),
    path('pago/', pago, name='pago'),
    path('translate/', translate, name='translate'),
    path('comprobante/', comprobante, name='comprobante'),
    path('registro/', registro, name='registro'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('user_page/', user_page, name='user_page'),
]