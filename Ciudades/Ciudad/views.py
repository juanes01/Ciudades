# Create your views here.

from django.http import HttpResponse
from django.template import loader

from django.shortcuts import render

# Instanciamos las vistas genéricas de Django
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Nos sirve para redireccionar despues de una acción revertiendo patrones de expresiones regulares
from django.urls import reverse

# Habilitamos el uso de mensajes en Django
from django.contrib import messages

# Habilitamos los mensajes para class-based views
from django.contrib.messages.views import SuccessMessageMixin

# Habilitamos los formularios en Django
from django import forms

from Ciudad.models import Region, Municipio


class RegionesListado(ListView):
    model = Region

class RegionesDetalle(DetailView):
    model = Region


class RegionesCrear(SuccessMessageMixin, CreateView):
    model = Region  # Llamamos a la clase 'Postres' que se encuentra en nuestro archivo 'models.py'
    form = Region  # Definimos nuestro formulario con el nombre de la clase o modelo 'Postres'
    fields = "__all__"  # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos
    success_message = 'Region Creada Correctamente !'  # Mostramos este Mensaje luego de Crear un Postre

    # Redireccionamos a la página principal luego de crear un registro o postre
    def get_success_url(self):
        return reverse('leer')  # Redireccionamos a la vista principal 'leer'


class RegionesActualizar(SuccessMessageMixin, UpdateView):
    model = Region  # Llamamos a la clase 'Postres' que se encuentra en nuestro archivo 'models.py'
    form = Region  # Definimos nuestro formulario con el nombre de la clase o modelo 'Postres'
    fields = "__all__"  # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos
    success_message = 'Region Actualizada Correctamente !'  # Mostramos este Mensaje luego de Editar un Postre

    # Redireccionamos a la página principal luego de actualizar un registro o postre
    def get_success_url(self):
        return reverse('leer')  #


class RegionesEliminar(SuccessMessageMixin, DeleteView):
    model = Region
    form = Region
    fields = "__all__"

    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self):
        success_message = 'Region Eliminada Correctamente !'  # Mostramos este Mensaje luego de Editar un Postre
        messages.success(self.request, (success_message))
        return reverse('leer')  # Redireccionamos a la vista principal 'leer'



def index(request):
    lista_regiones = None
    lista_regiones = Region.objects.all()
    # template = loader.get_template('/Templates/regiones.html')
    template = loader.get_template('regiones.html')
    context = {
        'lista_regiones': lista_regiones,
    }
    return HttpResponse(template.render(context, request))
    # return HttpResponse("vffddgfn")