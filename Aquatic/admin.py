from django.contrib import admin

from Aquatic.models import Alumno, Ropa, Clases

@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'edad', 'domicilio')

@admin.register(Ropa)
class RopaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tamaño', 'precio')

@admin.register(Clases)
class ClasesAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'duracion', 'maestro')