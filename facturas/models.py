from django.db import models



class Cliente(models.Model):
    nombre = models.CharField(max_length=60, blank=False)
    telefono = models.CharField(max_length=10, blank=False)
    
    def __str__(self):
        return self.nombre


class Factura(models.Model):
    fecha = models.DateField(blank=False)
    clienteID = models.ForeignKey(Cliente, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.clienteID




class Inventario(models.Model):
    nombre = models.CharField(max_length=60, blank=False)
    descripcion = models.TextField(max_length=300, blank=False)
    precio = models.IntegerField()

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    inventarioID = models.ForeignKey(Inventario, null=True, on_delete=models.CASCADE)
    facturaID = models.ForeignKey(Factura, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.inventarioID.nombre

class DetalleFactura(models.Model):
    cantidad = models.IntegerField()
    facturaID = models.ForeignKey(Factura, null=False, on_delete=models.CASCADE)
    ProductoID = models.ForeignKey(Inventario, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.ProductoID