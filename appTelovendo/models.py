from django.contrib.auth.models import AbstractUser, Group
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    # Campos adicionales
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    tipo_usuario = models.CharField(max_length=100, blank=True)
    
    
    def __str__(self):
        return self.username


class Login(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username
    
grupo_cliente, _ = Group.objects.get_or_create(name='Cliente')
grupo_vendedor, _ = Group.objects.get_or_create(name='Vendedor')
