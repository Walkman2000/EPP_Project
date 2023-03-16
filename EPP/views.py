from django.shortcuts import render, HttpResponse, redirect
from django.db import connection, DatabaseError, DataError, IntegrityError, InterfaceError, InternalError, ProgrammingError, OperationalError, Error, NotSupportedError
from .models import Productos, Proveedores, Categorias, Compras, detallesCompras, Ventas, detallesVentas, Imagenes
from django.template.exceptions import TemplateDoesNotExist, TemplateSyntaxError
from django.utils.datastructures import MultiValueDictKeyError
# Create your views here.
def index_admin(request):
    contexto = {}
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT ap.id, ap.nombre, ap.precio, ap.categoria_id, ap.descripcion,ap.cantidad,ap.prov_id, am.imagen FROM Productos as ap left join Imagenes as am ON ap.imagen_id = am.id")
        provs = Proveedores.objects.all()
        prods =  cursor.fetchall()
        categorias = Categorias.objects.all()
        imagenes = Imagenes.objects.all()
        for imagen in imagenes:
            print(imagen.id, imagen.imagen)
        contexto["productos"] = prods
        contexto["proveedores"] = provs
        contexto["categorias"]  = categorias
        contexto["imagenes"] = imagenes
        return render(request, "admin/productos.html", contexto)
    except (TemplateDoesNotExist, TemplateSyntaxError) as e:
        print(e)
        return HttpResponse("Ocurrió un error")

def mostrar_productos(request):
    cursor = connection.cursor()
    productos = cursor.callproc("mostrar_productos")
    print("Productos:",productos.fetchall() )
 
    return render(request, 'productos.html',{
        'productos': productos
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
        # print(producto_guardado)
        cursor = connection.cursor()
        cursor.callproc("agregar_producto", [request.POST.get("producto"),request.POST.get("precio"), Categorias.objects.get(id=request.POST.get("sl-categorias")), request.POST.get("descripcion"), request.POST.get("cantidad"), Proveedores.objects.get(id=request.POST.get("sl_proveedores"))])
        imagen = Imagenes.objects.create(imagen = request.FILES["imagen"])
        c = cursor.fetchone()[0]
        print("Imagen: ", imagen)
        cursor2 = connection.cursor()
        cursor2.execute("UPDATE Productos SET imagen_id = %s WHERE id = %s" % (imagen.pk, c))
        print("ID: ",c)
        return redirect("home")
# Pendiente checar en front
def actulizar_producto(request):
    print("ID:", request.POST.get("id_prod"))
    print("Nombre:", request.POST.get("producto"))
    print("Producto:", request.POST.get("precio"))
    print("Descrip:", request.POST.get("descripcion"))
    print("Cantidad",request.POST.get("cantidad"))
    print("Categoria",request.POST.get("sl-categorias"))
    print("Proveedor",request.POST.get("sl_proveedores"))
    
    Productos.objects.filter(pk=request.POST.get("id_prod")).update(nombre=request.POST.get("producto"), precio=request.POST.get("precio"), descripcion=request.POST.get("descripcion"), cantidad=request.POST.get("cantidad"))

    try:
        if request.FILES['imagen']:
            p = Productos.objects.get(pk=request.POST.get("id_prod"))
            p.imagen = request.FILES['imagen']
            p.save()
    except MultiValueDictKeyError:
        pass

    return redirect("home")

def eliminar_producto(request, id_producto):
    print(id_producto)
    Productos.objects.get(id=id_producto).delete()
    return redirect("home")
    
def agregar_proveedor(request):
    if request.method == 'POST':
        print(request.POST.get("proveedor"))
        print(request.POST.get("email"))
        print(request.POST.get("telefono"))
        cursor = connection.cursor()
        cursor.callproc("agregar_proveedor", [request.POST.get("proveedor"), request.POST.get("telefono"), request.POST.get("email")])
        return redirect("home")
    
    else:
        return render(request, "admin/addProveedor.html")
    

def compras_admin(request):
    try:
        cursor = connection.cursor()
        # compras = cursor.execute("SELECT id_compra, fecha, u.usuario  FROM Compras as c, Usuarios as u where c.usuario_id = u.id")
        cursor.execute("SELECT id_compra, fecha, u.usuario  FROM Compras inner join Usuarios as u")
        c = cursor.fetchall()
        print("Compras: ", c)
        return render(request, "admin/compras.html", {
            'compras' : c
        })
    except AttributeError as e:
        print(e)
        return HttpResponse("Problem")
    
def ventas_admin(request):
    try:
        cursor = connection.cursor()
        # compras = cursor.execute("SELECT id_compra, fecha, u.usuario  FROM Compras as c, Usuarios as u where c.usuario_id = u.id")
        cursor.execute("SELECT monto, fecha, u.usuario  FROM Compras inner join Usuarios as u")
        c = cursor.fetchall()
        print("Ventas: ", c)
        return render(request, "admin/ventas.html", {
            'ventas' : c
        })
    except AttributeError as e:
        print(e)
        return HttpResponse("Problem")
    
def detalles_compras(request):

    return render(request, "admin/detallesCompras.html")

def detalles_ventas(request):

    return render(request, "admin/detallesVenta.html")

