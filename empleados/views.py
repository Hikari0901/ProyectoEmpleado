from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy #line: 84
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

#importar el modelo empleados
from .models import Empleado

#importar el forms
from .forms import EmpleadoForm


# Create your views here.
class InicioView(TemplateView):
    """Vista pagina de inicio"""
    template_name='inicio.html'
    

#1.listar todos los empleados de la empresa
class ListaAllEmpleados(ListView):
    template_name= 'empleados/list_all.html'
    #ordena por el nombre
    ordering = 'first_name'
    #selecciona la cant de elementos y los distribuye en pags
    paginate_by= 6
    model = Empleado
    
    def get_queryset(self):
        palabra_clave= self.request.GET.get("kword",'')
        lista= Empleado.objects.filter(
            #icontanes sirve para ver la relacion de la palabra clave
            first_name__icontains=palabra_clave
        )
        return lista
    
#2.listar todos los empleados que pertenecen a una area de la empresa
class ListByAreaEmpleado(ListView):
    template_name= 'empleados/list_by_area.html'
    context_object_name='empleados'
    
    def get_queryset(self):
        #el codigo que se necesita, llamamos a la parte de la BD
        area = self.kwargs['short_name']
        lista= Empleado.objects.filter(
            departamento__short_name =area
        )
        return lista
    
    
#3.listar los empleados por palabra clave

class ListEmpleadoByKword(ListView):
    """Listar empleados por palabra clave"""
    template_name= 'empleados/by_kword.html'
    context_object_name = "empleados"
    
    def get_queryset(self):
        print("""""""""""")
        palabra_clave = self.request.GET.get("kword",'')
        lista = Empleado.objects.filter(
            first_name = palabra_clave
        )
        
        return lista
    
#4. listar las habilidades de un empleado 
class ListaHabilidadesEmpleado(ListView):
    template_name='empleados/habilidades.html'
    context_object_name = 'habilidades'
    
    def get_queryset(self):
        empleado = Empleado.objects.get(id=10)
        return empleado.Habilidades.all()



class EmpleadoDetailView(DetailView):
    template_name="empleados/detail_empleados.html"
    model = Empleado
    
    def get_context_data(self, **kwargs):
        context=super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context['titulo'] = 'Empleado del mes'
        return context
    
#create success
class SuccessView(TemplateView):
    template_name = 'empleados/Success/success_create.html'
#create el success_update
class SuccessUpdate(TemplateView):
    template_name='empleados/Success/success_update.html'
#crear el succes eliminate
class SuccessEliminate(TemplateView):
    template_name='empleados/Success/delete_success.html'

    
    
#crear un empleado desde el front
class EmpleadoCreateView(CreateView):
    template_name = 'empleados/add.html'
    model = Empleado
    #se llama a todos los campos
    form_class= EmpleadoForm
    ##fields = ['first_name', 'last_name', 'job', 'departamento', 'Habilidades']#'__all__'
    #llamas a la url por el nombre que le has puesto
    success_url = reverse_lazy('empleado_app:empleados_admin')
    
    def form_valid(self, form):
        #valida la informacion
        empleado = form.save(commit=False)
        #guarda la informacion
        empleado.save()
        #el form_valid hace que sean campos validos o obligatorios
        return super(EmpleadoCreateView,self).form_valid(form)
    
#actualiza el empleado desde el front
class EmpleadoUpdateView(UpdateView):
    template_name='empleados/update.html'
    model = Empleado
    fields = ['first_name', 'last_name', 'job', 'departamento', 'Habilidades']
    success_url = reverse_lazy('empleado_app:SuccessUpdate')
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print("Metodo Post")
        print(request.POST)
        return super().post(request, *args, **kwargs)
    
    def form_valid(self, form):
        form
        return super(EmpleadoUpdateView, self).form_valid(form)


#permite eliminar empleado desde el front
class EmpleadoDeleteView(DeleteView):
    template_name='empleados/delete.html'
    model=Empleado
    success_url = reverse_lazy('empleado_app:SuccessEliminte')
    