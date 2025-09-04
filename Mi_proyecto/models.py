from django.db import models


# Create your models here.
class Evento(models.Model):
    nombre = models.CharField(max_length=80)
    descripcion = models.TextField()
    capacidad = models.IntegerField()
    lugar = models.CharField(max_length=130)
    artistas = models.CharField(max_length=100)
    n_boletas = models.IntegerField()
    costo = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    fecha = models.DateField()
    hora = models.TimeField()
   
    vestimenta = models.CharField( max_length=50)
    flyer = models.ImageField(upload_to="flyers/", blank=True, null=True)
    flyer_patrocinadores = models.ImageField(upload_to="patrocinadores/", null=True, blank=True)  # 👈 nuevo
    
    def mostrar_costo(self):
        if not self.costo or self.costo == 0:
            return "Gratis"
        return f"${self.costo:,.0f}"
    mostrar_costo.short_description = "Costo"
    
    def __str__(self):
        return self.nombre
    
    
    
    
    