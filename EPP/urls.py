from django.urls import path
from .views import *


urlpatterns = [
    path("productos", index_admin, name="home"),
    path("agregar_producto", agregar_productos, name="addProduct"),
]