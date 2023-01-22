from django.urls import path
from Aquatic.views import pagina_de_inicio, crear_alumno, crear_ropa, crear_clase, lista_alumnos, lista_clases, lista_ropa

urlpatterns = [
    path('pagina_inicio/', pagina_de_inicio),
    path('crear-alumno/', crear_alumno),
    path('crear-ropa/', crear_ropa),
    path('crear-clase/', crear_clase),
    path('lista-alumnos/', lista_alumnos),
    path('lista-ropa/', lista_ropa),
    path('lista-clases/', lista_clases)

]