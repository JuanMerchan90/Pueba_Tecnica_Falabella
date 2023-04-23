from rest_framework import serializers
from .models import Cliente


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ('id','numero_documento','nombre','apellido','correo','telefono','created_at')
        read_only_fields = ('id','created_at',)

