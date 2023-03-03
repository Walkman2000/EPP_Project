
from django.contrib import admin

from .models import Proveedores, Productos, Clientes, Usuarios, Compras, Ventas, detallesCompras, detallesVentas, MovimientosAlmacen, Carrito
# Register your models here.

@admin.register(Productos)
class ProductosTabla(admin.ModelAdmin):
    list_display = ['nombre','precio','categoria','descripcion','cantidad','prov','imagen']

@admin.register(detallesCompras)
class DetallesComprasTabla(admin.ModelAdmin):
    list_display = ['id', 'cantidad','producto','compra']
@admin.register(Compras)
class ComprasTabla(admin.ModelAdmin):
    list_display = ['id_compra', 'fecha','usuario','monto']

@admin.register(Clientes)
class ClientesTabla(admin.ModelAdmin):
    list_display = ['nombre','direccion','telefono','email']

@admin.register(Ventas)
class ClientesTabla(admin.ModelAdmin):
    list_display = ['fecha', 'usuario', 'monto']

@admin.register(detallesVentas)
class ClientesTabla(admin.ModelAdmin):
    list_display = ['cantidad', 'producto', 'venta']
    
@admin.register(Proveedores)
class ProveedoresTabla(admin.ModelAdmin):
    list_display = ['nombre', 'telefono', 'email']

@admin.register(Usuarios)
class UsuariosTabla(admin.ModelAdmin):
    list_display = ['usuario', 'contraseña', 'estado', 'cliente']

@admin.register(Carrito)
class UsuariosTabla(admin.ModelAdmin):
    list_display = ['monto', 'producto']

@admin.register(MovimientosAlmacen)
class MovimientosAlmacenTabla(admin.ModelAdmin):
    list_display = ['tipoMovimiento','Motivo']    