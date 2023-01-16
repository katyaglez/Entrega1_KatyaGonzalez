from django import forms

class AlumnoForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    edad = forms.IntegerField()
    domicilio = forms.CharField(max_length=50)