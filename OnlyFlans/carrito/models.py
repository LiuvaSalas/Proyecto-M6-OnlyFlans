from django.db import models
from django.contrib.auth.models import User
from web.models import Flan

class Carrito(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='carrito')

    def __str__(self):
        return f"Carrito de {self.usuario.username}"

class ItemCarrito(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE, related_name='items')
    flan = models.ForeignKey(Flan, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

    def subtotal(self):
        return self.flan.price * self.cantidad

    def __str__(self):
        return f"{self.cantidad} x {self.flan.name}"