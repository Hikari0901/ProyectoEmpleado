from django.db import models
from departamentos.models import Departamento
#importacion ckeditor
from ckeditor.fields import RichTextField
# Create your models here.
class Habilidades(models.Model):
    habilidad = models.CharField('Habildiad', max_length=50)
    def __str__(self):
        return str(self.id) + '-' + self.habilidad
    
    class Meta:
        verbose_name_plural= 'Habilidades Empleados'
        verbose_name = 'Habilidad'
        
class Empleado(models.Model):
    """Modelo para la tabla empleado"""
    #Contador
    #administrador
    #economista
    #otro
    JOB_CHOICES=(
        ('0','CONTADOR'),
        ('1','ADMINISTRADOR'),
        ('2','ECONOMISTA'),
        ('3','OTRO'),
        
    )
    #atributos
    first_name = models.CharField('Nombre', max_length=50)
    last_name  =models.CharField('Apellidos', max_length=50)
    job = models.CharField('Trabajo', max_length=1, choices=JOB_CHOICES)
    image = models.ImageField(upload_to='empleado', blank=True, null=True)
    
    def __str__(self):
        return str(self.id) + ' ' + self.first_name + '-' + self.last_name + '-' + self.job
    #creacion del forenkey
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    Habilidades = models.ManyToManyField(Habilidades)
    hoja_vida=RichTextField()