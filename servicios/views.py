from django.shortcuts import render
from servicios.models import Servicios
from servicios.forms import ServiciosForm

def servicios_list(request):
    servicios = Servicios.objects.filter(is_active = True)
    context = {
        'servicios':servicios
    }
    return render(request, 'servicios/servicios-list.html', context=context)

def servicios_create(request):
    if request.method == 'GET':
        context = {
            'form': ServiciosForm()
        }

        return render(request, 'servicios/servicios-create.html', context=context)

    elif request.method == 'POST':
        form = ServiciosForm(request.POST)
        if form.is_valid():
            Servicios.objects.create(
                nombre = form.cleaned_data['nombre'],
                duracion = form.cleaned_data['duracion'],
                maestro = form.cleaned_data['maestro'],
                condition = form.cleaned_data['condition'],
            )
            context= {
                'message': 'Servicio creado exitosamente'
            }
            return render(request, 'servicios/servicios-create.html', context=context)
        else:
            context= {
                'form_errors': form.errors,
                'form': ServiciosForm()
            }
            return render(request, 'servicios/servicios-create.html', context=context)

def servicios_update(request, id):
    servicios = Servicios.objects.get(id=id)


    if request.method == 'GET':
        context = {
            'form': ServiciosForm(
                initial={
                    'nombre':servicios.nombre,
                    'duracion':servicios.duracion,
                    'maestro':servicios.maestro,
                    'condition':servicios.condition,
                }
            )
        }

        return render(request, 'servicios/servicios-update.html', context=context)

    elif request.method == 'POST':
        form = ServiciosForm(request.POST)
        if form.is_valid():
            servicios.update(
                nombre = form.cleaned_data['nombre'],
                duracion = form.cleaned_data['duracion'],
                maestro = form.cleaned_data['maestro'],
                condition = form.cleaned_data['condition'],
            )
            context= {
                'message': 'Servicio actualizado exitosamente'
            }
        else:
            context= {
                'form_errors': form.errors,
                'form': ServiciosForm()
            }
            return render(request, 'servicios/servicios-update.html', context=context)