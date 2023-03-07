from django.shortcuts import render, HttpResponse, redirect
from django.db import connection, DatabaseError, DataError, IntegrityError, InterfaceError, InternalError, ProgrammingError, OperationalError, Error, NotSupportedError
from .models import Productos, Proveedores, Categorias
from django.template.exceptions import TemplateDoesNotExist, TemplateSyntaxError
# Create your views here.
def index_admin(request):
    contexto = {}
    try:
        provs = Proveedores.objects.all()
        prods =  Productos.objects.all()
        categorias = Categorias.objects.all()
        contexto["productos"] = prods
        contexto["proveedores"] = provs
        contexto["categorias"]  = categorias
        print("Productos:", prods)
        return render(request, "admin/productos.html", contexto)
    except (TemplateDoesNotExist, TemplateSyntaxError) as e:
        print(e)
        return HttpResponse("Ocurrió un error")

def mostrar_productos(request):
    cursor = connection.cursor()
    clientes = cursor.execute("SELECT * FROM Clientes")
    print("Clientes:",clientes.fetchall() )
 
    return render(request, 'productos.html',{
        'clientes':clientes
    })

def agregar_productos(request):
    if request.method == 'POST':
        print(request.POST.get("producto"))
        print(request.POST.get("precio"))
        print(request.POST.get("categoria"))
        print(request.POST.get("descripcion"))
        print(request.POST.get("cantidad"))
        print(request.POST.get("sl-categorias"))
        # try
        Productos.objects.create(nombre=request.POST.get("producto"), precio=request.POST.get("precio"), categoria=Categorias.objects.get(id=request.POST.get("sl-categorias")), descripcion=request.POST.get("descripcion"), cantidad=request.POST.get("cantidad"), prov=Proveedores.objects.get(id=request.POST.get("sl_proveedores")), imagen=request.FILES["imagen"])
        # print(producto_guardado)
        return redirect("home")

# Pendiente checar en front
def actulizar_producto(request):
    producto = Productos.objects.update(nombre=request.POST("producto"), 
                                        precio=request.POST("precio"), 
                                        categoria=Categorias.objects.get(id=request.POST.get("sl-categorias")), descripcion=request.POST("descripcion"),
                                        cantidad=request.POST("cantidad"), 
                                        prov=Proveedores.objects.get(id=request.POST.get("sl_proveedores")), imagen=request.FILES["imagen"])

    producto.save()

    return redirect("home")
    

def eliminar_producto(request, id_producto):
    print(id_producto)
    Productos.objects.get(id=id_producto).delete()
    return redirect("home")

    