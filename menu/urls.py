from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('caja/', views.caja, name='caja'),
    path('cocina/', views.cocina, name='cocina'),
    path('cierre/', views.cierre_caja, name='cierre_caja'),
    path('api/registrar-venta/', views.registrar_venta, name='registrar_venta'),
    path('api/pedidos-pendientes/', views.pedidos_pendientes, name='pedidos_pendientes'),
    path('api/marcar-entregado/<int:venta_id>/', views.marcar_entregado, name='marcar_entregado'),
    path('api/cierre-caja/', views.api_cierre_caja, name='api_cierre_caja'),
    path('api/anular-venta/<int:venta_id>/', views.anular_venta, name='anular_venta'),
]