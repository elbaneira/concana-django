from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('caja/', views.caja, name='caja'),
    path('cocina/', views.cocina, name='cocina'),
    path('entregado/<int:venta_id>/', views.marcar_entregado, name='marcar_entregado'),
    path('cierre/', views.cierre_caja, name='cierre_caja'),
]
