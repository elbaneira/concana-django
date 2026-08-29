import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from django.db.models import Sum
from .models import Categoria, Producto, Venta

def inicio(request):
    categorias = Categoria.objects.prefetch_related('productos').all()
    return render(request, 'menu/inicio.html', {'categorias': categorias})

def caja(request):
    productos = Producto.objects.filter(disponible=True)
    return render(request, 'menu/caja.html', {'productos': productos})

def cocina(request):
    return render(request, 'menu/cocina.html')

def cierre_caja(request):
    return render(request, 'menu/cierre_caja.html')

@csrf_exempt
def registrar_venta(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            nueva_venta = Venta.objects.create(
                cliente=data.get('cliente', ''),
                total=int(data.get('total', 0)),
                metodo_pago=data.get('metodo_pago', 'Efectivo'),
                palabra_ticket=data.get('palabra_ticket', 'Ticket'),
                detalle_items=data.get('detalle_items', '')
            )
            return JsonResponse({'status': 'ok', 'venta_id': nueva_venta.id})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Método no permitido'}, status=405)

def pedidos_pendientes(request):
    ventas = Venta.objects.filter(estado='Completada').order_by('fecha_hora')
    datos = []
    
    productos_db = {p.nombre.lower(): p.estacion for p in Producto.objects.all()}

    for v in ventas:
        items_bar = []
        items_cocina = []
        items_parrilla = []

        if v.detalle_items:
            lista_items = [i.strip() for i in v.detalle_items.split(',') if i.strip()]
            for item in lista_items:
                partes = item.split('x ', 1)
                nombre_prod = partes[1].lower() if len(partes) > 1 else item.lower()
                estacion_asignada = productos_db.get(nombre_prod, '')

                if estacion_asignada == 'Bar' or any(w in nombre_prod for w in ['terremoto', 'bebida', 'jugo', 'cerveza', 'borgoña', 'pisco']):
                    items_bar.append(item)
                elif estacion_asignada == 'Parrilla' or any(w in nombre_prod for w in ['chorip', 'anticucho', 'asado', 'parri']):
                    items_parrilla.append(item)
                else:
                    items_cocina.append(item)

        # Solo incluir si no está todo listo en sus respectivas estaciones
        todo_entregado = True
        if items_bar and not v.bar_entregado:
            todo_entregado = False
        if items_cocina and not v.cocina_entregado:
            todo_entregado = False
        if items_parrilla and not v.parrilla_entregado:
            todo_entregado = False

        if not todo_entregado:
            datos.append({
                'id': v.id,
                'cliente': v.cliente or 'Sin nombre',
                'palabra_ticket': v.palabra_ticket,
                'bar_items': items_bar,
                'cocina_items': items_cocina,
                'parrilla_items': items_parrilla,
                'bar_entregado': v.bar_entregado,
                'cocina_entregado': v.cocina_entregado,
                'parrilla_entregado': v.parrilla_entregado,
                'hora': v.fecha_hora.strftime('%H:%M')
            })

    return JsonResponse({'pedidos': datos})

@csrf_exempt
def marcar_entregado(request, venta_id):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8')) if request.body else {}
            estacion = data.get('estacion', 'TODOS')
            venta = Venta.objects.get(id=venta_id)

            if estacion == 'BAR':
                venta.bar_entregado = True
            elif estacion == 'COCINA':
                venta.cocina_entregado = True
            elif estacion == 'PARRILLA':
                venta.parrilla_entregado = True
            else:
                venta.bar_entregado = True
                venta.cocina_entregado = True
                venta.parrilla_entregado = True

            venta.save()
            return JsonResponse({'status': 'ok'})
        except Venta.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Pedido no encontrado'}, status=404)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Método no permitido'}, status=405)

def api_cierre_caja(request):
    hoy = timezone.now().date()
    ventas_hoy = Venta.objects.filter(fecha_hora__date=hoy, estado='Completada')

    total_general = ventas_hoy.aggregate(Sum('total'))['total__sum'] or 0
    total_efectivo = ventas_hoy.filter(metodo_pago='Efectivo').aggregate(Sum('total'))['total__sum'] or 0
    total_maquina = ventas_hoy.filter(metodo_pago='Máquina').aggregate(Sum('total'))['total__sum'] or 0
    total_transferencia = ventas_hoy.filter(metodo_pago='Transferencia').aggregate(Sum('total'))['total__sum'] or 0

    return JsonResponse({
        'fecha': hoy.strftime('%d/%m/%Y'),
        'total_general': total_general,
        'total_efectivo': total_efectivo,
        'total_maquina': total_maquina,
        'total_transferencia': total_transferencia,
        'cantidad_ventas': ventas_hoy.count()
    })
@csrf_exempt
def anular_venta(request, venta_id):
    if request.method == 'POST':
        try:
            venta = Venta.objects.get(id=venta_id)
            
            # Cambiamos el estado a Anulada para que no afecte el cierre ni salga en cocina
            venta.estado = 'Anulada'
            venta.save()
            
            return JsonResponse({'status': 'ok', 'message': f'Venta #{venta_id} anulada correctamente'})
        except Venta.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'La venta no existe'}, status=404)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
            
    return JsonResponse({'status': 'error', 'message': 'Método no permitido'}, status=405)

import qrcode
from django.http import HttpResponse
from io import BytesIO

def generar_qr(request):
    # Enlace principal de tu app en Render
    url_app = "https://concana-django.onrender.com/"
    
    # Crear el objeto QR
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url_app)
    qr.make(fit=True)

    # Convertir la imagen a formato PNG en memoria
    img = qr.make_image(fill_color="black", back_color="white")
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    
    return HttpResponse(buffer.getvalue(), content_type="image/png")