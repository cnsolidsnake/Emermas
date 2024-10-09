from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth import get_user_model

# Clase de usuario personalizada
class Usuario(AbstractUser):
    correo = models.EmailField(unique=True)
    # Puedes agregar otros campos si es necesario

    def __str__(self):
        return self.username

# Modelo de Especialidad para citas
class Especialidad(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

# Modelo de Cita para gestionar las citas médicas
class Cita(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    estado = models.CharField(max_length=10, choices=[('Pendiente', 'Pendiente'), ('Cancelada', 'Cancelada'), ('Confirmada', 'Confirmada')])

    def __str__(self):
        return f"{self.usuario} - {self.especialidad} - {self.fecha} {self.hora}"

# Modelo de Historial Médico para almacenar los registros médicos
class HistorialMedico(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    descripcion = models.TextField()
    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Historial de {self.usuario} - {self.fecha}"
