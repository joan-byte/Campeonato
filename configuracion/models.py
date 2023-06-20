from django.db import models

# Create your models here.
class caracteristicas_campeonato(models.Model):
    nombre_campeonato = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='tournament_logos/')
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    lugar = models.CharField(max_length=50)
    num_partidas = models.IntegerField()
    serieB = models.BooleanField(default=False)
    puntos_totales =models.BooleanField(default=False)
    