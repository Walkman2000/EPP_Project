from django.db import models
from django.conf import settings
class Proveedores(models.Model):
    nombre = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return f'{self.nombre}, {self.telefono}, {self.email} '
    class Meta:
        db_table = 'Proveedores'

class Productos(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.FloatField()
    categoria = models.CharField(max_length=30)
    descripcion = models.TextField()
    cantidad = models.FloatField()
    prov = models.ForeignKey(Proveedores, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="productos")

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
    telefono = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return f'{self.nombre}, {self.direccion}, {self.telefono}, {self.direccion}'

    class Meta:
        db_table = 'Clientes'

class Usuarios(models.Model):
    usuario = models.CharField(max_length=50)
    contraseña = models.CharField(max_length=50, null=False, blank=False, default="")
    estado = models.BooleanField(default=True)
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.usuario}, {self.contraseña}, {self.estado}, {self.cliente}'

    class Meta:
        db_table = 'Usuarios'

class Compras(models.Model):
    id_compra = models.CharField(max_length=10, default="")
    fecha = models.DateField()
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE, default="")
    monto = models.FloatField(default=0)

    def __str__(self):
        return f'{self.id_compra}'
    class Meta:
        db_table = 'Compras'

class Ventas(models.Model):
    fecha = models.DateField()
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
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