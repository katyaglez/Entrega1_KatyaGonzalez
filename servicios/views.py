from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView
from servicios.models import Servicios
from servicios.forms import ServiciosForm

def servicios_list(request):
    servicios = Servicios.objects.filter(is_active = True)
    context = {
        'servicios':servicios
    }
    return render(request, 'servicios/servicios-list.html', context=context)

class ServiciosListView(ListView):
    model = Servicios
    template_name = 'servicios/servicios-list.html'
    queryset = Servicios.objects.filter(is_active = True)


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

class ServiciosCreateView(CreateView):
    model = Servicios
    template_name = 'servicios/servicios-create.html'
    fields = '__all__'
    success_url = '/servicios/servicios-list/'


def servicios_update(request, pk):
    servicios = Servicios.objects.get(id=pk)

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
            servicios.nombre = form.cleaned_data['nombre']
            servicios.duracion = form.cleaned_data['duracion']
            servicios.maestro = form.cleaned_data['maestro']
            servicios.condition = form.cleaned_data['condition']
            servicios.save()
            
            context= {
                'message': 'Servicio actualizado exitosamente'
            }
        else:
            context= {
                'form_errors': form.errors,
                'form': ServiciosForm()
            }
        return render (request, 'servicios/servicios-update.html', context=context)
    

class ServiciosDeleteView(DeleteView):
    model = Servicios
    template_name = 'servicios/servicios-delete.html'
    success_url = '/servicios/servicios-list/'