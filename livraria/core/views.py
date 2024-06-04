# core/views.py

from rest_framework import viewsets
from .models import Fornecedor, Livro, Cliente, Pedido, PedidoLivro, Balconista, PedidoCliente, PedidoFornecedor
from .serializers import FornecedorSerializer, LivroSerializer, ClienteSerializer, PedidoSerializer, PedidoLivroSerializer, BalconistaSerializer, PedidoClienteSerializer, PedidoFornecedorSerializer
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Bem-vindo à Livraria</h1><p>API disponível em <a href='/api/'>/api/</a></p>")

class FornecedorViewSet(viewsets.ModelViewSet):
    queryset = Fornecedor.objects.all()
    serializer_class = FornecedorSerializer

class LivroViewSet(viewsets.ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

class PedidoLivroViewSet(viewsets.ModelViewSet):
    queryset = PedidoLivro.objects.all()
    serializer_class = PedidoLivroSerializer

class BalconistaViewSet(viewsets.ModelViewSet):
    queryset = Balconista.objects.all()
    serializer_class = BalconistaSerializer

class PedidoClienteViewSet(viewsets.ModelViewSet):
    queryset = PedidoCliente.objects.all()
    serializer_class = PedidoClienteSerializer

class PedidoFornecedorViewSet(viewsets.ModelViewSet):
    queryset = PedidoFornecedor.objects.all()
    serializer_class = PedidoFornecedorSerializer
