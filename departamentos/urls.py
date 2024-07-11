from django.contrib import admin
from django.urls import path

#llamar la vista
from . import views

app_name = "departamento_app"


urlpatterns = [
    path('departamento-lista/',views.DepartamentoListView.as_view(),name='departamento_list'),
    path('newdepartamento/',views.NewDepartamentoView.as_view(),name='nuevo_departamento'),
]
