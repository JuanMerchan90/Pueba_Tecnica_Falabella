from .models import Cliente
from rest_framework import viewsets, permissions
from .serializers import ClienteSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ClienteSerializer

    # filter_fields = ('nome', 'email')
    # search_fields = ('nome', 'email')
    # ordering_fields = ('nome', 'email')
    # ordering = ('nome', 'email')
    # def perform_create(self, serializer):
    #     serializer.save(usuario=self.request.user)