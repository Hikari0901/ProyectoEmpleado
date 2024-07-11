from django.contrib import admin
#importacion de empleados
from .models import Empleado, Habilidades
# Register your models here.
admin.site.register(Habilidades)

class EmpleadoAdmin(admin.ModelAdmin):
    list_display=(
        'id',
        'first_name',
        'last_name',
        'departamento',
        'job',
        'full_name',
    )
    #
    def full_name(self, obj):
        #print(obj.first_name)
        return obj.first_name + ' ' + obj.last_name
    
    #Funciones especiales en el admin
    search_fields=('first_name',)
    list_filter = ('departamento','job','Habilidades')
    #filter horizontal
    filter_horizontal=('Habilidades',)
    
admin.site.register(Empleado, EmpleadoAdmin)

