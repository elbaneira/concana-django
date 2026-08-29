from django.contrib import admin
from .models import Categoria, Producto, Venta

admin.site.register(Categoria)
admin.site.register(Producto)

@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ('id', 'fecha_hora', 'total', 'metodo_pago', 'cliente', 'estado', 'palabra_ticket')
    list_filter = ('estado', 'metodo_pago', 'fecha_hora')
    list_editable = ('estado',) # <--- Permite cambiar a "Anulada" con un solo clic desde la lista