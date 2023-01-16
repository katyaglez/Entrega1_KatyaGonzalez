from django.shortcuts import render
from django.http import HttpResponse

from Aquatic.models import Alumno, Ropa, Clases
from Aquatic.forms import AlumnoForm

def crear_alumno(request):
    if request.method == 'GET':
        context = {
            'form': AlumnoForm()
        }

        return render(request, 'crear_alumno.html', context=context)

    elif request.method == 'POST':
        form = AlumnoForm(request.POST)
        if form.is_valid():
            Alumno.objects.create(
                nombre=form.cleaned_data['nombre'],
                edad=form.cleaned_data['edad'],
                domicilio=form.cleaned_data['domicilio'],
            )
            context= {
                'message': 'Alumno creado exitosamente'
            }
            return render(request, 'crear_alumno.html', context=context)
        else:
            context= {
                'form_errors': form.errors,
                'form': AlumnoForm()
            }
            return render(request, 'crear_alumno.html', context=context)


def crear_ropa(request):
    ropa_nueva = Ropa.objects.create( nombre = 'Sandalias', tamaño = 'Talla 4', precio = '100 pesos')
    return HttpResponse('Haz creado una nueva prenda')

def crear_clase(request):
    clase_nueva = Clases.objects.create( nombre = 'Natación', duracion = '1 hora', maestro = 'Marco Díaz')
    return HttpResponse('Haz creado una nueva clase')




def pagina_de_inicio(request):
    return render (request, 'pagina_inicio.html', context={})

def lista_alumnos(request):
    todos_los_alumnos = Alumno.objects.all()
    context = {
        'alumnos': todos_los_alumnos,
    }
    return render (request, 'pagina_alumnos.html', context = context)

def lista_ropa(request):
    todas_las_ropas = Ropa.objects.all()
    context = {
        'ropa': todas_las_ropas,
    }
    return render (request, 'pagina_ropa.html', context = context)

def lista_clases(request):
    todas_las_clases = Clases.objects.all()
    context = {
        'clases': todas_las_clases,
    }
    return render (request, 'pagina_clases.html', context = context)