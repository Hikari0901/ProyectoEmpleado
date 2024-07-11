from django.db import models

# Create your models here.
class Departamento(models.Model):
    name = models.CharField('Nombre', max_length=50)
    short_name = models.CharField('Nombre Corto', max_length=20)
    anulate = models.BooleanField('Anulado',default=False)
    
    class Meta:
        verbose_name= 'Mi Departamento'
        verbose_name_plural= 'Areas de la Empresa'
        ordering = ['-name']#ordena
        
    
    #hacemos que aparezca mas entendible los nombres 
    def __str__(self):
        return str(self.id) + '-' + self.name + "-" + self.short_name
    