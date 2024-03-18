from django.db import models


class CategoriaProducto(models.Model):
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    descripcion = models.TextField()
    categoria = models.ForeignKey(CategoriaProducto, on_delete=models.PROTECT)
    imagen = models.ImageField(upload_to='productos', null=True )

    def __str__(self):
        return self.nombre

class Pedido(models.Model):
    nombre = models.CharField(max_length=50)
    envio = models.TextField()
    monto = models.FloatField()
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre
