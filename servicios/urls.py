from django.urls import path
from servicios.views import servicios_list, servicios_create, servicios_update, ServiciosListView, ServiciosCreateView, ServiciosDeleteView

urlpatterns = [
    path('servicios-list/', ServiciosListView.as_view(), name='servicios_list'),
    path('servicios-create/', ServiciosCreateView.as_view(), name='servicios_create'),
    path('servicios-update/<int:pk>/', servicios_update, name='servicios_update'),
    path('servicios-delete/<int:pk>/', ServiciosDeleteView.as_view(), name='servicios_delete'),
]