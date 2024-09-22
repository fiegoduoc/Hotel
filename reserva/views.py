from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from reserva.forms import CreateUserForm, AuthForm
from django.contrib.auth.decorators import login_required


def login_user(request):
    #if request.user.is_authenticated:
        #return redirect('index')
    #if:
        if request.method == "POST":
            form = AuthForm(data=request.POST)
            if form.is_valid():
                username = request.POST.get('username')
                password = request.POST.get('password')
                user = authenticate(request, username=username, password=password)

                if user is not None:
                    login(request, user)
                    return redirect('pago')
                else:
                    messages.info(request, 'Usuario o contraseña incorrecta')
        else:
            form = AuthForm()
            messages.error(request, 'Error al iniciar sesión')

        return render(request, 'login.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect('index')

def registro(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user=form.cleaned_data.get('username')
                messages.success(request, 'Cuenta creada para ' + user)
                return redirect('login')
        else:
            form = CreateUserForm()
            messages.error(request, 'Error al crear la cuenta')
    return render(request, 'registro.html', {'form': form})

def user_page(request):
    return render(request, 'user_page.html')

#One-Page Web Application
def index(request):
    return render(request, 'index.html')


def catalogo_premium(request):
    return render(request, 'catalogo_premium.html')


def catalogo_turista(request):
    return render(request, 'catalogo_turista.html')


def reserva(request):
    return render(request, 'reservas/reserva.html')


def disponibilidad(request):
    return render(request, 'reservas/disponibilidad.html')


@login_required(login_url='login')
def pago(request):
    return render(request, 'reservas/pago.html')


def translate(request):
    return render(request, 'english/index.html')

@login_required(login_url='login')
def comprobante(request):
    return render(request, 'reservas/comprobante.html')
