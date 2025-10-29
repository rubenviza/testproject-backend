from django.urls import path
from .views import clientes_list, get_cliente

urlpatterns = [
    path("clientes/", clientes_list),
    path("cliente/", get_cliente),
]
