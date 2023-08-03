from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm

usuarios = [
    {
        'nombre' : "Juan",
        'apellido' : "Perez",
        'edad' : "35",
        'mail' : "juan.perez@example.com",
        'telefono' : "1234567890"
    },
    {
        'nombre' : "Maria",
        'apellido' : "Lopez",
        'edad' : "28",
        'mail' : "maria.lopez@example.com",
        'telefono' : "9876543210"
    },
    {
        'nombre' : "Laura",
        'apellido' : "Ramirez",
        'edad' : "31",
        'mail' : "laura.ramirez@example.com",
        'telefono' : "7890123456"
    },
    {
        'nombre' : "Carlos",
        'apellido' : "Sanchez",
        'edad' : "42",
        'mail' : "carlos.sanchez@example.com",
        'telefono' : "4567890123"
    },
    {
        'nombre' : "Pedro",
        'apellido' : "Gonzalez",
        'edad' : "39",
        'mail' : "pedro.gonzalez@example.com",
        'telefono' : "3210987654"
    },
]
# Create your views here.

def index(request):
    return render(request, 'appTelovendo/index.html')

def clientes(request):
    auxiliar = {
        'usuarios' : usuarios
    }
    return render(request, 'appTelovendo/clientes.html', auxiliar)

def registrarse(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        correo = request.POST.get('correo')
        contraseña = request.POST.get('contraseña')
        repita_contraseña = request.POST.get('repita_contraseña')
        nombre_usuario = nombre
        nuevo_usuario, creado = CustomUser.objects.get_or_create(username=nombre, email=correo)
        if not creado:
            return render(request, 'appTelovendo/registrarse.html')
        nuevo_usuario.set_password(contraseña)
        nuevo_usuario.first_name = nombre
        nuevo_usuario.last_name = apellido
        nuevo_usuario.save()
        #Captura el grupo seleccionado
        grupo_id = request.POST.get('grupo')
        grupo = Group.objects.get(pk=grupo_id)
        nuevo_usuario.groups.add(grupo)
        return redirect('iniciar_sesion')
    return render(request, 'appTelovendo/registrarse.html') 
@login_required
def iniciar_sesion(request):
        from django.contrib.auth import authenticate, login
        
def iniciar_sesion(request):
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            #obtener los datos del formulario de inicio de sesion
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            #Autenticar al usuario
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('bienvenida')
    else:
        form = LoginForm    


    return render(request, 'registro/login.html', {'form':form})


def bienvenida(request):
    user = request.user
    if user.is_authenticated and user.first_name:
        first_name = user.first_name
        return render(request, 'appTelovendo/bienvenida.html', {'first_name': first_name})
    else:
        return render(request, 'bienvenida')
    
def exit(request):
    logout(request)
    return redirect('mensaje')