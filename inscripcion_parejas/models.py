from django.db import models


# Create your models here.
class Parejas(models.Model):
    Jugador1 = models.CharField(max_length=50)
    Jugador2 = models.CharField(max_length=50)
    Club_pertenencia = models.CharField(max_length=50)
    Numero_pareja = models.IntegerField(auto_created=1)   #numero de pareja

    def pareja(self):
        cadena = "{0} {1}"
        return cadena.format(self.Jugador1, self.Jugador2)
    
pareja = Parejas(Jugador1="Jugador1", Jugador2="Jugador2")  #creamos una pareja

