# core/models.py

from django.db import models

class Fornecedor(models.Model):
    codigo = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=50)
    cep = models.CharField(max_length=20)
    telefone = models.CharField(max_length=20)
    cnpj = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

class Livro(models.Model):
    codigo = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    codfornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

class Cliente(models.Model):
    codigo = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=50)
    cep = models.CharField(max_length=20)
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

class Pedido(models.Model):
    codigo = models.AutoField(primary_key=True)
    datapddido = models.DateField()
    listalivro = models.ManyToManyField(Livro, through='PedidoLivro')
    quantidade = models.IntegerField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def calcular(self):
        self.valor = sum(item.livro.preco * item.quantidade for item in self.pedidolivro_set.all())
        self.save()

class PedidoLivro(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    quantidade = models.IntegerField()

class Balconista(models.Model):
    nomeusuario = models.CharField(max_length=100, unique=True)
    senha = models.CharField(max_length=100)
    nivelacesso = models.CharField(max_length=50)

class PedidoCliente(models.Model):
    codcliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    dataromessa = models.DateField()

class PedidoFornecedor(models.Model):
    codfornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)
    datarecebimento = models.DateField()
