from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    ESTACIONES = [
        ('Bar', 'Bar (Bebidas/Terremotos)'),
        ('Cocina', 'Cocina (Empanadas/Papas)'),
        ('Parrilla', 'Parrilla (Choripanes/Anticuchos)'),
    ]

    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.IntegerField()
    disponible = models.BooleanField(default=True)
    estacion = models.CharField(max_length=20, choices=ESTACIONES, default='Cocina')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='productos')

    def __str__(self):
        return f"{self.nombre} [{self.estacion}] - ${self.precio}"


class Venta(models.Model):
    METODOS_PAGO = [
        ('Efectivo', 'Efectivo'),
        ('Máquina', 'Máquina'),
        ('Transferencia', 'Transferencia'),
    ]

    ESTADOS = [
        ('Completada', 'Completada'),
        ('Anulada', 'Anulada'),
    ]

    cliente = models.CharField(max_length=100, blank=True, null=True)
    total = models.IntegerField()
    metodo_pago = models.CharField(max_length=20, choices=METODOS_PAGO, default='Efectivo')
    palabra_ticket = models.CharField(max_length=100)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='Completada')
    
    # Estados de despacho independientes por área
    bar_entregado = models.BooleanField(default=False)
    cocina_entregado = models.BooleanField(default=False)
    parrilla_entregado = models.BooleanField(default=False)

    detalle_items = models.TextField(blank=True, null=True)
    fecha_hora = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Venta #{self.id} (${self.total})"