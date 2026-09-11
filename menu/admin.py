from django.contrib import admin
from .models import Venta

@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'cajero', 'curso_cajero', 'turno', 'cantidad', 'total', 'medio_pago', 'fecha_hora')
    list_filter = ('curso_cajero', 'turno', 'medio_pago')
    search_fields = ('cliente', 'cajero__username')
    ordering = ('-fecha_hora',)