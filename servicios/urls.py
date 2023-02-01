from django.urls import path
from servicios.views import servicios_list, servicios_create, servicios_update

urlpatterns = [
    path('servicios-list/', servicios_list, name='servicios_list'),
    path('servicios-create/', servicios_create, name='servicios_create'),
    path('servicios-update/<int:pk>/', servicios_update, name='servicios_update'),
]