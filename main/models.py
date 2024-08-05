from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Avion(models.Model):
  modelo = models.CharField(max_length=45)
  ciudad_actual = models.CharField(max_length=45, default='santiago')
  def __str__(self):
    return f'{self.modelo}'
  
class Viaje(models.Model):
  origenes = (('santiago','Santiago - Chile'), ('lima', 'Lima - Perú'), ('buenos aires', 'Buenos Aires - Argentina'), ('la paz', 'La Paz - Bolivia'), ('quito', 'Quito - Ecuador'))
  destinos = (('santiago','Santiago - Chile'), ('lima', 'Lima - Perú'), ('buenos aires', 'Buenos Aires - Argentina'), ('la paz', 'La Paz - Bolivia'), ('quito', 'Quito - Ecuador'))
  codigo = models.CharField(max_length=45, primary_key=True)
  origen = models.CharField(max_length=45, choices=origenes)
  fecha = models.DateField()
  destino = models.CharField(max_length=45, choices=destinos)
  ciudad_actual = models.CharField(max_length=45)
  estado = models.CharField(max_length=45)
  avion = models.ForeignKey(Avion, on_delete =models.RESTRICT, related_name='viajes')
  
class Pasajero(models.Model):
  vacunas = (('sinovac', 'Sinovac'), ('astrazeneca', 'Astrazeneca'), ('pfizer', 'Pfizer'), ('cancino', 'Cancino'), ('otra', 'Otra'))
  nombre = models.CharField(max_length=45)
  rut = models.CharField(max_length=45, unique=True)
  vacuna = models.CharField(max_length=45, choices = vacunas)
  fecha_nacimiento = models.DateField()
  viaje = models.ForeignKey(Viaje, on_delete =models.RESTRICT, related_name='pasajeros')
