from django.db import models


class CategoriaProducto(models.Model):
    nombre = models.CharField(max_length=100)
    pass

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    pass


class Pedido(models.Model):
    pass
