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

    path('regiones/', views.RegionesListado.as_view(template_name="regiones/index.html"), name='leerRegion'),

    path('municipios/', views.MunicipioListado.as_view(template_name="municipios/index.html"), name='leerMunicipio'),


    path('regiones/detalle/<int:pk>', views.RegionesDetalle.as_view(template_name="regiones/detalles.html"), name='detalles'),

    path('municipios/detalle/<int:pk>', views.MunicipioDetalle.as_view(template_name="municipios/detalles.html"), name='detalles'),


    path('regiones/crear', views.RegionesCrear.as_view(template_name="regiones/crear.html"), name='crearRegion'),

    path('municipios/crear', views.MunicipiosCrear.as_view(template_name="municipios/crear.html"), name='crearMunicipio'),

    path('regiones/editar/<int:pk>', views.RegionesActualizar.as_view(template_name="regiones/actualizar.html"),
         name='actualizarRegion'),

    path('municipios/editar/<int:pk>', views.MunicipiosActualizar.as_view(template_name="municipios/actualizar.html"),
         name='actualizarMunicipio'),

    path('regiones/eliminar/<int:pk>', views.RegionesEliminar.as_view(), name='eliminarRegiones'),

    path('municipios/eliminar/<int:pk>', views.MunicipiosEliminar.as_view(), name='eliminarMunicipios'),
]
