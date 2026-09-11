from django.db import models
from django.contrib.auth.models import User

CURSOS = [
    ('2E', 'Segundo E'),
    ('2F', 'Segundo F'),
    ('2D', 'Segundo D'),
]

PARRILLAS = [
    ('P1', 'Parrilla 1'),
    ('P2', 'Parrilla 2'),
    ('P3', 'Parrilla 3'),
    ('P4', 'Parrilla 4'),
]

TURNOS = [
    ('T1', 'Turno 1 - Mañana'),
    ('T2', 'Turno 2 - Tarde'),
    ('T3', 'Turno 3 - Cierre'),
]

MEDIOS_PAGO = [
    ('EFECTIVO', 'Efectivo'),
    ('TRANSFERENCIA', 'Transferencia'),
]

class Venta(models.Model):
    cajero = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ventas')
    curso_cajero = models.CharField(max_length=2, choices=CURSOS, verbose_name="Curso del Cajero")
    parrilla = models.CharField(max_length=2, choices=PARRILLAS, default='P1', verbose_name="Parrilla Asignada")
    turno = models.CharField(max_length=2, choices=TURNOS, verbose_name="Turno de Venta")
    cantidad = models.PositiveIntegerField(default=1, verbose_name="Cantidad de Anticuchos")
    total = models.PositiveIntegerField(default=0, verbose_name="Total a Pagar ($)")
    cliente = models.CharField(max_length=100, default="Cliente", verbose_name="Nombre del Cliente")
    
    medio_pago = models.CharField(max_length=15, choices=MEDIOS_PAGO, default='EFECTIVO', verbose_name="Medio de Pago")
    monto_recibido = models.PositiveIntegerField(default=0, verbose_name="Paga con ($)")
    vuelto = models.PositiveIntegerField(default=0, verbose_name="Vuelto ($)")
    
    completado = models.BooleanField(default=False, verbose_name="¿Entregado en Parrilla?")
    fecha_hora = models.DateTimeField(auto_now_add=True)

    def calcular_total(self):
        combos_3 = self.cantidad // 3
        sueltos = self.cantidad % 3
        return (combos_3 * 10000) + (sueltos * 4000)

    def save(self, *args, **kwargs):
        self.total = self.calcular_total()
        if self.medio_pago == 'EFECTIVO' and self.monto_recibido >= self.total:
            self.vuelto = self.monto_recibido - self.total
        else:
            self.vuelto = 0
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Venta #{self.id} - {self.cantidad} Anticuchos - Total: ${self.total}"
    
# Dentro de menu/models.py, agrega este campo a la clase Venta:

    
    # ... (los demás campos se mantienen igual)