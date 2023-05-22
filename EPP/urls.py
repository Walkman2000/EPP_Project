from django.urls import path
from .views import *


urlpatterns = [
    path("productos", index_admin, name="home"),
    path("agregar_producto", agregar_productos, name="addProduct"),
    path("actualizar_producto", actulizar_producto, name="updateProduct"),
    path("eliminar_producto/<int:id_producto>", eliminar_producto, name="deleteProduct"),
    path("agregar_proveedor", agregar_proveedor, name="addProveedor"),
    #path("compras", compras_admin, name="buysAdmin"),
    path("ventas", ventas_admin, name="sellsAdmin"),
    path("compras_admin", compras_admin, name="buysAdmin"),
    path("detalles_ventas/<int:id_venta>", detalles_ventas, name="sellsDetails"),
    path("generar_reportes/<int:id_venta>", reports, name="generateReport")

]