from django.db import models

# Create your models here.
class Cliente(models.Model):
    numero_documento = models.CharField(max_length=20)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo  = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)


