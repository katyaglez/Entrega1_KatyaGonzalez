from django import forms

from servicios.models import Servicios

class ServiciosForm(forms.Form):
    nombre = forms.CharField(max_length=30)
    duracion = forms.CharField(max_length=15)
    maestro = forms.CharField(max_length=30)
    condition = forms.CharField(max_length=50)


    # class ServiciosForm(forms.ModelForm):

    #     class Meta:
    #         model = Servicios
    #         fields = '__all__'