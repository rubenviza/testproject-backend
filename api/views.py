from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

clientes = [
    {"id": 1, "nombre": "Juan Pérez", "email": "juan@example.com"},
    {"id": 2, "nombre": "Ana López", "email": "ana@example.com"},
    {"id": 3, "nombre": "Carlos Ruiz", "email": "carlos@example.com"},
]


@api_view(["GET"])
def clientes_list(request):
    return Response(clientes)


@api_view(["POST"])
def get_cliente(request):
    clienteX = next((c for c in clientes if c["id"] == request.data.get("id")), None)

    if clienteX is None:
        return Response(
            {"error": "Cliente no encontrado"}, status=status.HTTP_404_NOT_FOUND
        )

    return Response(clienteX)
