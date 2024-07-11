
from django.contrib import admin
from django.urls import path, include

#IMPORTAR SETTINGS para imagenes
from django.conf import settings
from django.conf.urls.static import static

from home.views import IndexView, PruebaListView, ModeloPruebaListView
urlpatterns = [
    #ruta principal admin
    path('admin/', admin.site.urls),
    
    #incluir rutas empleados
    path('', include('empleados.urls')),
    
    #incluir urls home
    path('', include('home.urls')),
    
    #incluir urls departamento
    path('', include('departamentos.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
