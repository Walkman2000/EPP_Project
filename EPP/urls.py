from django.urls import path
from .views import *


urlpatterns = [
    path("productos", index_admin, name="home"),
    path("agregar_producto", agregar_productos, name="addProduct"),
    path("actualizar_producto", actulizar_producto, name="updateProduct"),
    path("eliminar_producto/<int:id_producto>", eliminar_producto, name="deleteProduct"),
    path("agregar_proveedor", agregar_proveedor, name="addProveedor"),
    path("compras", compras_admin, name="buysAdmin"),
    path("ventas", ventas_admin, name="sellsAdmin"),
    path("detalles_compras", detalles_compras, name="buysDetails"),
    path("detalles_ventas", detalles_ventas, name="sellsDetails")

]