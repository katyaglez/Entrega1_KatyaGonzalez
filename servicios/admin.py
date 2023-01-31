from django.contrib import admin

from servicios.models import Servicios

@admin.register(Servicios)
class ServiciosAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'duracion', 'maestro')