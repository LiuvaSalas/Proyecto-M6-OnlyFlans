from django.shortcuts import render

#INDEX - Landing Page
#def index(request):
#    return render(request, "index.html", {})

def about(request):
    return render(request, "about.html", {})

def welcome(request):
    return render(request, "welcome.html", {})

def index(request):
    postres = [
        {"nombre": "Flan de Chocolate", "descripcion": "Flan con sabor a chocolate negro", "ruta": "assets/img/productos/flan-chocolate-negro.jpg"},
        {"nombre": "Flan de Vainilla", "descripcion": "Flan sabor Vainilla con topping de Chocolate Blanco", "ruta": "assets/img/productos/flan-toping-chocolate-blanco.avif"},
        {"nombre": "Fran Tradicional", "descripcion": "Flan Tradicional", "ruta": "assets/img/productos/flan-tradicional.jpg"}
    ]
    contexto = {"postres": postres}
    return render(request, "index.html", contexto)