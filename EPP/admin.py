from django.contrib import admin

from .models import Proveedores, Productos, Clientes, Usuarios, Compras, Ventas, detallesCompras, detallesVentas, MovimientosAlmacen
# Register your models here.

admin.site.register((Proveedores, Productos, Clientes, Usuarios, Compras, Ventas, detallesCompras, detallesVentas, MovimientosAlmacen))



