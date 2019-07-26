"""Ciudades URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from .Ciudad import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='regiones'),

    path('regiones/', views.RegionesListado.as_view(template_name="regiones/index.html"), name='leer'),

    # La ruta 'detalles' en donde mostraremos una página con los detalles de un postre o registro
    path('regiones/detalle/<int:pk>', views.RegionesDetalle.as_view(template_name="regiones/detalles.html"), name='detalles'),

    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo postre o registro
    path('regiones/crear', views.RegionesCrear.as_view(template_name="regiones/crear.html"), name='crear'),
    #
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un postre o registro de la Base de Datos
    path('regiones/editar/<int:pk>', views.RegionesActualizar.as_view(template_name="regiones/actualizar.html"),
         name='actualizar'),
    #
    # La ruta 'eliminar' que usaremos para eliminar un postre o registro de la Base de Datos
    path('regiones/eliminar/<int:pk>', views.RegionesEliminar.as_view(), name='eliminar'),
]
