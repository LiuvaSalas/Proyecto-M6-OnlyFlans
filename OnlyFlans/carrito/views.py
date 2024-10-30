from django.shortcuts import render, redirect, get_object_or_404
from .models import Carrito, ItemCarrito
from web.models import Flan  # Importa el modelo Flan
from web.views import index
from django.http import HttpResponseRedirect
from django.urls import reverse


def carrito(request):
    if request.user.is_authenticated:
        carrito = Carrito.objects.filter(usuario=request.user).first()
        total = sum(item.subtotal() for item in carrito.items.all()) if carrito else 0
        return render(request, "carrito.html", {"carrito": carrito, "total": total})
    else:
        return render(
            request,
            "carrito.html",
            {"error": "Debes iniciar sesión para ver tu carrito."},
        )


def agregar_al_carrito(request, flan_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))

    flan = get_object_or_404(Flan, id=flan_id)
    carrito, creado = Carrito.objects.get_or_create(usuario=request.user)

    item, item_creado = ItemCarrito.objects.get_or_create(carrito=carrito, flan=flan)
    if not item_creado:
        item.cantidad += 1
        item.save()
    return redirect("index")


def eliminar_del_carrito(request, item_id):
    item = get_object_or_404(ItemCarrito, id=item_id)
    if item.carrito.usuario == request.user:
        item.delete()  # Elimina el item del carrito
    return redirect("carrito")  # Redirige a la vista del carrito
