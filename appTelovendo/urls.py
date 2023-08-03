from django.urls import path
from . import views

# app_name = 'app'

urlpatterns = [
    path('', views.index, name='mensaje'),
    path('clientes/', views.clientes, name='clientes' ),
    path('registrarse/', views.registrarse, name='registrarse' ),
    path('iniciar_sesion/', views.iniciar_sesion, name='iniciar_sesion' ),
    path('bienvenida/', views.bienvenida, name='bienvenida' ),
    path('exit/', views.exit, name = 'exit'),   
    
]
