from django.db import models

# Create your models here.
class Evento(models.Model):
    nombre = models.CharField(max_length=80)
    descripcion = models.TextField()
    capacidad = models.IntegerField()
    lugar = models.CharField(max_length=130)
    artistas = models.CharField(max_length=100)
    n_boletas = models.IntegerField()
    costo = models.BooleanField(default=False)
    fecha = models.DateField()
    hora = models.TimeField()
    publicidad = models.CharField(max_length=50)
    vestimenta = models.CharField( max_length=50)
    flyer = models.ImageField(upload_to="flyers/", blank=True, null=True)
    
    def __str__(self):
        return self.nombre
    
    
    
    
    