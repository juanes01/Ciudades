# Create your views here.

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

from Ciudad.models import Region, Municipio

from .forms import numeroLetraForm
from django.http import HttpResponseRedirect
from django.shortcuts import render


dict = {1: 'A',        2: 'B',        3: 'C',        4: 'D',        5: 'E',        6: 'F',
        7: 'G',        8: 'H',        9: 'I',        10: 'J',        11: 'K',        12: 'L',
        13: 'M',        14: 'N',        15: 'Ñ',        16: 'O',        17: 'P',        18: 'Q',
        19: 'R',        20: 'S',        21: 'T',        22: 'U',        23: 'V',        24: 'W',
        25: 'X',        26: 'Y',        27: 'Z',
        }


class RegionesListado(ListView):
    model = Region

class RegionesDetalle(DetailView):
    model = Region

class MunicipioListado(ListView):
    model = Municipio

class MunicipioDetalle(DetailView):
    model = Municipio


class RegionesCrear(SuccessMessageMixin, CreateView):
    model = Region
    form = Region
    fields = "__all__"
    success_message = 'Region Creada Correctamente !'

    def get_success_url(self):
        return reverse('leerRegion')

class MunicipiosCrear(SuccessMessageMixin, CreateView):
    model = Municipio
    form = Municipio
    fields = "__all__"
    success_message = 'Municipio Creado Correctamente !'

    def get_success_url(self):
        return reverse('leerMunicipio')


class RegionesActualizar(SuccessMessageMixin, UpdateView):
    model = Region
    form = Region
    fields = "__all__"
    success_message = 'Region Actualizada Correctamente !'


    def get_success_url(self):
        return reverse('leerRegion')


class MunicipiosActualizar(SuccessMessageMixin, UpdateView):
    model = Municipio
    form = Municipio
    fields = "__all__"
    success_message = 'Municipio Actualizado Correctamente !'


    def get_success_url(self):
        return reverse('leerMunicipio')


class RegionesEliminar(SuccessMessageMixin, DeleteView):
    model = Region
    form = Region
    fields = "__all__"

    def get_success_url(self):
        success_message = 'Region Eliminada Correctamente !'
        messages.success(self.request, (success_message))
        return reverse('leerRegion')


class MunicipiosEliminar(SuccessMessageMixin, DeleteView):
    model = Municipio
    form = Municipio
    fields = "__all__"

    def get_success_url(self):
        success_message = 'Municipio Eliminado Correctamente !'
        messages.success(self.request, (success_message))
        return reverse('leerMunicipio')



def index(request):

    letra = ''
    if request.method == 'POST':
        form = numeroLetraForm(request.POST)
        if form.is_valid():
            arrayLetras = []
            numero = form.cleaned_data['numero']
            if ((numero / 27) < 27):
                numeroi = int(numero / 27)
                numeroj = int(numero % 27)
                if numeroi > 0:
                    letra = dict.get(numeroi)
                if numeroj > 0:
                    letra = letra + dict.get(numeroj)
            else:
                cociente = numero
                while(True):
                    residuo = int(cociente % 27)
                    cociente = int(cociente / 27)
                    if cociente < 27:
                        arrayLetras.append(dict.get(residuo))
                        arrayLetras.append(dict.get(cociente))
                        break
                    else:
                        arrayLetras.append(dict.get(residuo))

                x = len(arrayLetras)
                for i in range(len(arrayLetras)):
                    letra = letra + arrayLetras[x-1]
                    x = x - 1
            return render(request, 'letrasynumeros.html', {'form': form, 'letra': letra})

    else:
        form = numeroLetraForm()

    return render(request, 'letrasynumeros.html', {'form': form, 'letra': letra})