# core/serializers.py

from rest_framework import serializers
from .models import Fornecedor, Livro, Cliente, Pedido, PedidoLivro, Balconista, PedidoCliente, PedidoFornecedor

class FornecedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fornecedor
        fields = '__all__'

class LivroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livro
        fields = '__all__'

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class PedidoLivroSerializer(serializers.ModelSerializer):
    class Meta:
        model = PedidoLivro
        fields = '__all__'

class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = '__all__'

class BalconistaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Balconista
        fields = '__all__'

class PedidoClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = PedidoCliente
        fields = '__all__'

class PedidoFornecedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = PedidoFornecedor
        fields = '__all__'
