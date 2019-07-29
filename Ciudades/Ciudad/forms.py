from django import forms

class numeroLetraForm(forms.Form):
    numero = forms.IntegerField(label='Ingrese el número')

    def clean_numero(self):
        numero_ingresado = self.cleaned_data['numero']
        if numero_ingresado <= 0:
            raise forms.ValidationError("Debes ingresar un valor positivo mayor a 0")
        return numero_ingresado