from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('add/',views.PruebaCreateView.as_view(),name='prueba_add'),
    path('prueba/', views.PruebaListView.as_view(), name='Prueba_lista')
]
