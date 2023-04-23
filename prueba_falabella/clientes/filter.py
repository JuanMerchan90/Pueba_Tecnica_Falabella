from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Cliente

class FiltrarCliente(APIView):

    def get(self, request, ced):
        cliente = Cliente.objects.all().filter(numero_documento=str(ced)).values()
        return Response(
            {
            'numero_documento': ced,
            'cliente': list(cliente)
            }
        )
