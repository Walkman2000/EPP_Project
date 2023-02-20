from django.db import models

# Create your models here.
class Proveedores(models.Model):
    nombre = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()

    class Meta:
        db_table = 'Proveedores'

class Productos(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.FloatField()
    categoria = models.CharField(max_length=30)
    descripcion = models.TextField()
    cantidad = models.FloatField()
    prov = models.ForeignKey(Proveedores, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="productos", null=True)

    class Meta:
        db_table = 'Productos'

class Clientes(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    telefono = models.IntegerField()
    email = models.EmailField()

    class Meta:
        db_table = 'Clientes'

class Compras(models.Model):
    nombre = models.CharField(max_length=50)
    fecha = models.DateField()

    class Meta:
        db_table = 'Compras'

class Usuarios(models.Model):
    usuario = models.CharField(max_length=50)
    contraseña = models.CharField(max_length=50)
    estado = models.BooleanField(default=True)
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'Usuarios'

class Ventas(models.Model):
    monto = models.IntegerField()
    fecha = models.DateField()
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Ventas'

class detallesVentas(models.Model):
    cantidad = models.FloatField()
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)    
    venta = models.ForeignKey(Ventas, on_delete=models.CASCADE)    
    
    class Meta:
        db_table = 'detallesVentas'

class detallesCompras(models.Model):
    cantidad = models.FloatField()
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    compra = models.ForeignKey(Compras, on_delete = models.CASCADE)

    class Meta:
        db_table = 'detallesCompras'

# class cuentasCobrar (models.Model):
#     monto = models.IntegerField()
#     venta = models.ForeignKey(Ventas, on_delete=models.CASCADE)
    
#     class Meta:
#         db_table = 'CuentasCobrar'


class MovimientosAlmacen(models.Model):
    tipoMovimiento = models.CharField(max_length=50)
    Motivo = models.CharField(max_length=100)
    class Meta:
        db_table = 'MovimientosAlmacen'