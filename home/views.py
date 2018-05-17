from django.shortcuts import render
from django.http import HttpResponse
from .Seguridad import Seguridad 

from .forms import RegisterForm

seguridad = Seguridad()

# Create your views here.
def home(request):
    return render(request, 'home/index.html')

def register(request):
    error = ''
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            clave = form.cleaned_data['clave']
            clave_conf = form.cleaned_data['conf_clave']
            error = seguridad.registrarUsuario(email, clave, clave_conf)
    else:
        form = RegisterForm()
    return render(request, 'home/registro.html', context={'form':form, 'error': error})

def login(request):
    return HttpResponse('')
    