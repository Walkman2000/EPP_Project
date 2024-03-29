from django.db import models
from django.conf import settings
from cuentas.models import CustomUser
class Proveedores(models.Model):
    nombre = models.CharField(max_length=50, null=True)
    telefono = models.CharField(max_length=20, null=True)
    email = models.EmailField(null=True)

    def __str__(self):
        return f'{self.id}'
    class Meta:
        db_table = 'Proveedores'

class Categorias(models.Model):
    categoria = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.id}'
    class Meta:
        db_table = 'Categorias'

class Imagenes(models.Model):
    imagen = models.ImageField(upload_to="imagenes", null=True, blank=True)

    class Meta:
        db_table = 'Imagenes'

class Productos(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.FloatField()
    descripcion = models.TextField()
    cantidad = models.FloatField()
    prov = models.ForeignKey(Proveedores, on_delete=models.CASCADE)
    imagen = models.ForeignKey(Imagenes, on_delete=models.CASCADE, default="", null=True)
    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE, default="")
    def __str__(self):
        return f'{self.nombre}'
    class Meta:
        db_table = 'Productos'

class Carrito (models.Model):
    monto = models.FloatField()
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.monto}, {self.producto}'
    class Meta:
        db_table = 'Carrito'

class Clientes(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return f'{self.nombre}, {self.direccion}, {self.telefono}, {self.direccion}'

    class Meta:
        db_table = 'Clientes'

class Compras(models.Model):
    id_compra = models.CharField(max_length=10, default="")
    fecha = models.DateField()
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default="")
    monto = models.FloatField(default=0)

    def __str__(self):
        return f'{self.id_compra}'
    class Meta:
        db_table = 'Compras'

class comprasAdmin(models.Model):
    fecha = models.DateField()
    monto  = models.FloatField(default=0)
    cantidad = models.FloatField(default=0)
    proveedores = models.ForeignKey(Proveedores, on_delete=models.CASCADE)
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)

    class Meta:
        db_table = 'comprasAdmin'

class Ventas(models.Model):
    fecha = models.DateField()
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    monto = models.FloatField(default=0)

    def __str__(self):
        return f'{self.pk} - {self.monto}'
    
    class Meta:
        db_table = 'Ventas'

class detallesVentas(models.Model):
    cantidad = models.FloatField()
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)    
    venta = models.ForeignKey(Ventas, on_delete=models.CASCADE)   
 
    def __str__(self):
        return f'{self.cantidad}, {self.producto}, {self.venta}'
    
    class Meta:
        db_table = 'detallesVentas'

class detallesCompras(models.Model):
    cantidad = models.FloatField()
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    compra = models.ForeignKey(Compras, on_delete = models.CASCADE)

    def __str__(self):
        return f'{self.cantidad}, {self.producto}, {self.compra}'
    
    class Meta:
        db_table = 'detallesCompras'

class MovimientosAlmacen(models.Model):
    tipoMovimiento = models.CharField(max_length=50)
    Motivo = models.CharField(max_length=100)
    class Meta:
        db_table = 'MovimientosAlmacen'