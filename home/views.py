from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse
from .Seguridad import Seguridad

from .forms import RegisterForm, IngresarForm
import urllib

seguridad = Seguridad()

# Create your views here.
def home(request):
    nombre = request.GET.get('nombre', 'Anonimo')
    return render(request, 'home/index.html', {'nombre': nombre})

def register(request):
    error = ''
    print(seguridad.usuariosRegistrados)
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            clave = form.cleaned_data['clave']
            print(clave)
            clave_conf = form.cleaned_data['conf_clave']
            error = seguridad.registrarUsuario(email, clave, clave_conf)
    else:
        form = RegisterForm()
    return render(request, 'home/registro.html', context={'form':form, 'error': error})

def login(request):
    error = ''
    print(seguridad.usuariosRegistrados)
    if request.method == 'POST':
        form = IngresarForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            clave = form.cleaned_data['clave']
            error = seguridad.ingresarUsuario(email, clave)
            if error == 'Usuario aceptado':
                return redirect(reverse('home:home') + '?nombre=' + email)
    else:
        form = IngresarForm()

    form = IngresarForm()
    return render(request, 'home/ingresar.html', context={'form':form, 'error': error})
