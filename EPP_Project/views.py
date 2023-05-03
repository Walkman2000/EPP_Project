from django.shortcuts import render, HttpResponse, redirect
from EPP.models import Productos
from django.db import connection
from EPP.models import Productos, Proveedores, Categorias, Compras, detallesCompras, Ventas, detallesVentas, Imagenes, comprasAdmin
from django.template.exceptions import TemplateDoesNotExist, TemplateSyntaxError

def index(request):
    contexto = {}
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT ap.id, ap.nombre, ap.precio, ap.categoria_id, ap.descripcion,ap.cantidad,ap.prov_id, am.imagen FROM Productos as ap left join Imagenes as am ON ap.imagen_id = am.id")
        provs = Proveedores.objects.all()
        prods =  cursor.fetchall()
        categorias = Categorias.objects.all()
        imagenes = Imagenes.objects.all()
        compras = comprasAdmin.objects.all()
        for imagen in imagenes:
            print(imagen.id, imagen.imagen)
        contexto["productos"] = prods
        contexto["proveedores"] = provs
        contexto["categorias"]  = categorias
        contexto["imagenes"] = imagenes
        contexto["compras"] = compras
        return render(request, "index.html", contexto)
    except (TemplateDoesNotExist, TemplateSyntaxError) as e:
        print(e)
        return HttpResponse("Ocurrió un error")
def pedidos(request):
    pedido = 'pedido1'

    context ={
        'pedido' : pedido
    }
    return render(request, 'pedidos.html', context)

def register(request):
    
    return render(request, 'register.html')