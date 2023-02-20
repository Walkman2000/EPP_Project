from django.urls import path
from .views import index_admin


urlpatterns = [
    path("productos", index_admin, name="home")
]