from django.shortcuts import render, HttpResponse, redirect
from django.db import connection, DatabaseError, DataError, IntegrityError, InterfaceError, InternalError, ProgrammingError, OperationalError, Error, NotSupportedError
from .models import Productos, Proveedores, Categorias, Compras, detallesCompras, Ventas, detallesVentas, Imagenes, comprasAdmin
from django.template.exceptions import TemplateDoesNotExist, TemplateSyntaxError
from django.utils.datastructures import MultiValueDictKeyError
import xlsxwriter
import datetime, io
from django.urls.exceptions import NoReverseMatch
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
        compras = comprasAdmin.objects.all()
        for imagen in imagenes:
            print(imagen.id, imagen.imagen)
        contexto["productos"] = prods
        contexto["proveedores"] = provs
        contexto["categorias"]  = categorias
        contexto["imagenes"] = imagenes
        contexto["compras"] = compras
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

def actulizar_producto(request):
    print("ID:", request.POST.get("id_prod"))
    print("Nombre:", request.POST.get("producto"))
    print("Producto:", request.POST.get("precio"))
    print("Descrip:", request.POST.get("descripcion"))
    print("Cantidad",request.POST.get("cantidad"))
    print("Categoria",request.POST.get("sl-categorias"))
    print("Proveedor",request.POST.get("sl_proveedores"))
    
    Productos.objects.filter(pk=request.POST.get("id_prod")).update(nombre=request.POST.get("producto"), 
                                                                    precio=request.POST.get("precio"),
                                                                    descripcion=request.POST.get("descripcion"), 
                                                                    cantidad=request.POST.get("cantidad"))

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
    
def compras_usuario(request):
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
        cursor.execute("SELECT Ventas.id, monto, fecha, u.usuario  FROM Ventas inner join Usuarios as u")
        c = cursor.fetchall()
        print("Ventas: ", c)
        return render(request, "admin/ventas.html", {
            'ventas' : c
        })
    except AttributeError as e:
        print(e)
        return HttpResponse("Problem")
    
def compras_admin(request):
    contexto = {}
    productos = Productos.objects.all()
    proveedores = Proveedores.objects.all()
    compras = comprasAdmin.objects.all().values('id','fecha','monto','cantidad', 'producto__nombre', 'proveedores__nombre')
    contexto["productos"] = productos
    contexto["proveedores"] = proveedores
    contexto["compras"] = compras

    if request.method == 'POST':
        # print("fecha" + request.POST.get("fecha"))
        # print("monto", request.POST.getlist("monto"))
        # print("cantidad", request.POST.getlist("cantidad"))
        # print("producto", request.POST.getlist("sl-producto"))
        # print("proveedor", request.POST.getlist("sl-proveedores"))

        for i in range(0, len(request.POST.getlist("sl-producto"))):
            cursor = connection.cursor()
            print(request.POST.getlist("sl-producto")[i])
            cursor.callproc("registrar_compra_admin", [request.POST.get("fecha"), request.POST.getlist("monto")[i], request.POST.getlist("cantidad")[i], request.POST.getlist("sl-producto")[i], request.POST.getlist("sl-proveedores")[i]])
        return redirect("buysAdmin")
    return render(request, "admin/compras_admin.html", contexto)

def detalles_compras_usuario(request):

    return render(request, "admin/detallesCompras.html")

def detalles_ventas(request, id_venta):
    contexto = {}
    try:
        detalles_ventas = detallesVentas.objects.filter(venta = id_venta).values('id','venta_id', 'producto__nombre', 'cantidad','producto__precio')
        contexto["detalles_ventas"] = detalles_ventas
        print(detalles_ventas)
        return render(request, "admin/detallesVenta.html", contexto)
    except NoReverseMatch as e:
        print(e)
        return HttpResponse("Algo salió mal")

def reports (request, id_venta):
    contexto = {}
    fecha_hoy = datetime.datetime.now()
    hoy = str(fecha_hoy.month) + "-" + str(fecha_hoy.day) + "-" + str(fecha_hoy.year)
    output = io.BytesIO()
    workbook = xlsxwriter.Workbook(output)
    hoja = workbook.add_worksheet('reporte')
    # obtencion de los datos
    resultado = detallesVentas.objects.filter(venta = id_venta).values('id','venta_id', 'producto__nombre', 'cantidad','producto__precio')
    print(resultado)
    contexto["detalles_ventas"] = detalles_ventas
    estilo_cuerpo = workbook.add_format({
        'font_name':'Arial',
        'border': 1
    })
    estilo_cuerpo.set_align("center")
    estilo_cuerpo.set_align("vcenter")

    estilo_encabezado = workbook.add_format({
        'bold': True,
    })
    estilo_encabezado.set_align("center")
    estilo_encabezado.set_align("vcenter")

    # Encabezado
    hoja.write(3,0, "ID VENTA", estilo_cuerpo)
    hoja.write(3,1, "PRODUCTO", estilo_cuerpo)
    hoja.write(3,2, "CANTIDAD", estilo_cuerpo)
    hoja.write(3,3, "PRECIO", estilo_cuerpo)
    hoja.write(3,4, "TOTAL", estilo_cuerpo)

    fila = 4 
    
    
    # Iteracion de datos

    for result in resultado: 
        hoja.write(fila,  0, result['venta_id'])
        hoja.write(fila,  1, result['producto__nombre'])
        hoja.write(fila,  2, result['cantidad'])
        hoja.write(fila,  3, result['producto__precio'])
        hoja.write(fila,  4, result['producto__precio']*result['cantidad'])
        fila += 1 

    workbook.close()
    output.seek(0)
    filename = f'reports{hoy}.xlsx'
    response = HttpResponse(
        output,
        content_type = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = f'attachment; filename = {filename}'
    return response

'''
Consulta para mostrar los detalles de las ventas
select v.id, p.nombre, p.precio, dv.cantidad, v.fecha from fluidos4_tienda_sigssmac.detallesVentas as dv 
inner JOIN fluidos4_tienda_sigssmac.Ventas as v 
ON dv.venta_id = v.id
inner JOIN fluidos4_tienda_sigssmac.Productos as p
on dv.producto_id = p.id and v.id = 4;
'''