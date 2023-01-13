from django.shortcuts import render
from django.http import HttpResponse

from Aquatic.models import Alumno, Ropa, Clases

def crear_alumno(request):
    nuevo_alumno = Alumno.objects.create( nombre = 'Katya', edad = 27, domicilio = 'Riva Palacio 123' ) 
    return HttpResponse('Haz creado un nuevo alumno')

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