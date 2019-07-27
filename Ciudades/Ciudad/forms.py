from django import forms

class numeroLetraForm(forms.Form):
    numero = forms.IntegerField(label='Ingrese el número')