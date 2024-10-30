from django.shortcuts import render,redirect, get_object_or_404
from .models import Carrito, ItemCarrito
from web.models import Flan  # Importa el modelo Flan
from django.contrib.auth.decorators import login_required

def carrito(request):
    carrito = Carrito.objects.filter(usuario=request.user).first()
    total = sum(item.subtotal() for item in carrito.items.all()) if carrito else 0
    return render(request, 'carrito.html', {'carrito': carrito, 'total': total})

def agregar_al_carrito(request, flan_id):
    flan = get_object_or_404(Flan, id=flan_id)
    carrito, creado = Carrito.objects.get_or_create(usuario=request.user)

    item, item_creado = ItemCarrito.objects.get_or_create(carrito=carrito, flan=flan)
    if not item_creado:
        item.cantidad += 1
        item.save()

    return redirect('carrito')


def ver_carrito(request):
    carrito = Carrito.objects.filter(usuario=request.user).first()
    total = sum(item.subtotal() for item in carrito.items.all()) if carrito else 0
    return render(request, 'carrito.html', {'carrito': carrito, 'total': total})