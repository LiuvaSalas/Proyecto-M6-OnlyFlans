from django.shortcuts import render
from .models import Flan


def index(request):
    flanes = Flan.objects.all()
    flanes_privados = Flan.objects.filter(is_private=True)
    flanes_publicos = Flan.objects.filter(is_private=False)

    contexto = {
        'flanes': flanes,
        'flanes_privados': flanes_privados,
        'flanes_publicos': flanes_publicos
    }
    return render(request, "index.html", contexto)


def about(request):
    return render(request, "about.html", {})


def welcome(request):
    flanes_privados = Flan.objects.filter(is_private=True)

    contexto = {
        'flanes_privados': flanes_privados,
    }
    return render(request, "welcome.html", contexto)

def contacto(request):
    return render(request, "contacto.html", {})
