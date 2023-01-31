from django import forms

class ServiciosForm(forms.Form):
    nombre = forms.CharField(max_length=30)
    duracion = forms.CharField(max_length=15)
    maestro = forms.CharField(max_length=30)
    condition = forms.CharField(max_length=50)