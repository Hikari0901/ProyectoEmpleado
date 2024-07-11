from django.contrib import admin
from django.urls import path
from . import views

#es el conjunto de todas las urls
app_name = "empleado_app"

#urls
urlpatterns = [
    path(
        '',
        views.InicioView.as_view(), 
        name='inicio'
        ),
    path(
        'listar-todo-empleados/',
        views.ListaAllEmpleados.as_view(),
        name='empleados_all'
        ),
    
    
    path('lista-by-area/<short_name>',views.ListByAreaEmpleado.as_view(),name='empleados_area'),
    path('buscar-empleado/',views.ListEmpleadoByKword.as_view()),
    path('ver-empleado/<pk>',views.EmpleadoDetailView.as_view(), name='empleado_detail'),
    path('lista-habilidades-empleado/',views.ListaHabilidadesEmpleado.as_view()),
    path('add-empleado/',views.EmpleadoCreateView.as_view(), name='empleado_add'),
    #finalidad del sig. codigo: 
    path('success/',views.SuccessView.as_view(), name = 'correcto'),
    path('eliminado-correcto/', views.SuccessEliminate.as_view(), name='SuccessEliminte'),
    path('actualizado-correcto/', views.SuccessUpdate.as_view(), name='SuccessUpdate'),
    path('update-empleado/<pk>/', views.EmpleadoUpdateView.as_view(), name='modificar_empleado'),
    path('delete-empleado/<pk>/', views.EmpleadoDeleteView.as_view(), name='eliminar_empleado'),
]
