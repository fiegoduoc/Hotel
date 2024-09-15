from django.shortcuts import render


#One Page Web Application
def index(request):
    return render(request, 'index.html')


def catalogo_premium(request):
    return render(request, 'catalogo_premium.html')


def catalogo_turista(request):
    return render(request, 'catalogo_turista.html')


def reserva(request):
    return render(request, 'reservas/reserva.html')


def signup(request):
    return render(request, 'SignUp.html')


def signin(request):
    return render(request, 'SignIn.html')
