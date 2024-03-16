from django.db import models


class CategoriaProducto(models.Model):
    nombre = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.IntegerField()
    descripcion = models.TextField()
    tipo = models.ForeignKey(CategoriaProducto, on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre

class Pedido(models.Model):
    pass