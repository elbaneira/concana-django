from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Venta

# Agregar esta vista para solucionar la ruta vacía
def inicio(request):
    return redirect('caja')

@login_required
def caja(request):
    if request.method == 'POST':
        cliente = request.POST.get('cliente', 'Cliente')
        curso_cajero = request.POST.get('curso_cajero')
        parrilla = request.POST.get('parrilla')
        turno = request.POST.get('turno')
        cantidad = int(request.POST.get('cantidad', 1))
        medio_pago = request.POST.get('medio_pago')
        monto_recibido = int(request.POST.get('monto_recibido', 0))

        Venta.objects.create(
            cliente=cliente,
            cajero=request.user,
            curso_cajero=curso_cajero,
            parrilla=parrilla,
            turno=turno,
            cantidad=cantidad,
            medio_pago=medio_pago,
            monto_recibido=monto_recibido
        )
        return redirect('caja')

   # Totales del equipo completo
    ventas = Venta.objects.all()
    pozo_comun = sum(v.total for v in ventas)
    total_anticuchos = sum(v.cantidad for v in ventas)
    ultimas_ventas = ventas.order_by('-fecha_hora')[:8]

    return render(request, 'menu/caja.html', {
        'pozo_comun': pozo_comun,
        'total_anticuchos': total_anticuchos,
        'ultimas_ventas': ultimas_ventas
    })

@login_required
def cocina(request):
    pedidos_pendientes = Venta.objects.filter(completado=False).order_by('fecha_hora')
    return render(request, 'menu/cocina.html', {'pedidos': pedidos_pendientes})

@login_required
def marcar_entregado(request, venta_id):
    venta = get_object_or_404(Venta, id=venta_id)
    venta.completado = True
    venta.save()
    return redirect('cocina')

# Agrega o reemplaza la función cierre_caja en menu/views.py

@login_required
def cierre_caja(request):
    ventas = Venta.objects.all()

    # Totales generales
    total_recaudado = sum(v.total for v in ventas)
    total_anticuchos = sum(v.cantidad for v in ventas)

    # Desglose por Medio de Pago
    total_efectivo = sum(v.total for v in ventas if v.medio_pago == 'EFECTIVO')
    total_transferencia = sum(v.total for v in ventas if v.medio_pago == 'TRANSFERENCIA')

    # Desglose por Turnos
    totales_turno = {
        'T1': sum(v.total for v in ventas if v.turno == 'T1'),
        'T2': sum(v.total for v in ventas if v.turno == 'T2'),
        'T3': sum(v.total for v in ventas if v.turno == 'T3'),
    }

    # Desglose por Cursos (Para auditoría si fuere necesario)
    totales_curso = {
        '2E': sum(v.total for v in ventas if v.curso_cajero == '2E'),
        '2F': sum(v.total for v in ventas if v.curso_cajero == '2F'),
        '2D': sum(v.total for v in ventas if v.curso_cajero == '2D'),
    }

    return render(request, 'menu/cierre_caja.html', {
        'total_recaudado': total_recaudado,
        'total_anticuchos': total_anticuchos,
        'total_efectivo': total_efectivo,
        'total_transferencia': total_transferencia,
        'totales_turno': totales_turno,
        'totales_curso': totales_curso,
        'ventas': ventas.order_by('-fecha_hora'),
    })
    return render(request, 'menu/cierre_caja.html', context)