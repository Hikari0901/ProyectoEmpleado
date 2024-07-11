from django.shortcuts import render
#importar de django la formview
from django.views.generic import ListView
from django.views.generic.edit import FormView
#import form
from .forms import NewDepartamentoForm
#importar el modelo departamento
from .models import Departamento
from empleados.models import Empleado
# Create your views here.

class DepartamentoListView(ListView):
    template_name='departamentos/lista.html'
    model = Departamento
    context_object_name = 'departamentos'

class NewDepartamentoView(FormView):
    template_name='departamentos/new_departamento.html'
    form_class= NewDepartamentoForm
    success_url = '/'
    
    def form_valid(self, form):
        print('estamos en el form valid*********')
        depa=Departamento(
            name = form.cleaned_data['departamento'],
            short_name= form.cleaned_data['short_name']
        )
        depa.save()
        nombre= form.cleaned_data['nombre']
        apellido=form.cleaned_data['apellidos']
        Empleado.objects.create(
            first_name= nombre,
            last_name= apellido,
            job='1',
            departamento = depa
        )
        return super(NewDepartamentoView, self).form_valid(form)
    
