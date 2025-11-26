from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

clientes = [
    {
        "id": 1,
        "nombre": "Juan Pérez",
        "email": "juan@example.com",
        "occupation": {"id": 22, "name": "Engineer"},
    },
    {
        "id": 2,
        "nombre": "Ana López",
        "email": "ana@example.com",
        "occupation": {"id": 33, "name": "Architect"},
    },
    {
        "id": 3,
        "nombre": "Carlos Ruiz",
        "email": "carlos@example.com",
        "occupation": {"id": 22, "name": "Engineer"},
    },
]


@api_view(["GET"])
def clientes_list(request):
    return Response(clientes)


@api_view(["POST"])
def get_cliente(request):
    cliente_id = int(request.data.get("id", 0))
    clienteX = next((c for c in clientes if c["id"] == cliente_id), None)

    if clienteX is None:
        return Response(
            {"error": "Cliente no encontrado"}, status=status.HTTP_404_NOT_FOUND
        )

    return Response(clienteX)
