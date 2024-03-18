from django.contrib import admin
from .models import *


class ProductoAdmin(admin.ModelAdmin):
    list_display = ["nombre","precio","categoria","descripcion"]
    list_editable = ["precio"]
    search_fields = ["nombre"]
    list_filter = ["categoria"]
    list_per_page = 10


# Register your models here.
admin.site.register(CategoriaProducto)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Pedido)