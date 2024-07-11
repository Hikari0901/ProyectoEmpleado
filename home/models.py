from django.db import models
#Comandos: python manage makemigrations, python manage migrate, (estos sirven para migrar el modelo a la BD)
# Create your models here.
class Prueba(models.Model):
    #crear los atributos
    titulo= models.CharField(max_length=30)#charfield es un campo normal de txt
    subtitulo= models.CharField(max_length=50)
    cantidad= models.IntegerField()#es un campo de numeros
    
    def __str__(self):
        return self.titulo + '-' + self.subtitulo