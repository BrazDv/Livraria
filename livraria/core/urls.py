# core/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FornecedorViewSet, LivroViewSet, ClienteViewSet, PedidoViewSet, PedidoLivroViewSet, BalconistaViewSet, PedidoClienteViewSet, PedidoFornecedorViewSet, home

router = DefaultRouter()
router.register(r'fornecedores', FornecedorViewSet)
router.register(r'livros', LivroViewSet)
router.register(r'clientes', ClienteViewSet)
router.register(r'pedidos', PedidoViewSet)
router.register(r'pedido-livros', PedidoLivroViewSet)
router.register(r'balconistas', BalconistaViewSet)
router.register(r'pedido-clientes', PedidoClienteViewSet)
router.register(r'pedido-fornecedores', PedidoFornecedorViewSet)

urlpatterns = [
    path('', home, name='home'),
    path('api/', include(router.urls)),
]
