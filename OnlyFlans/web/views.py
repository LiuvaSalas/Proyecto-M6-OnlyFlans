from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import ContactForm, Flan
from .forms import ContactFormForm, ContactFormModelForm


def index(request):
    flanes = Flan.objects.all()
    flanes_privados = Flan.objects.filter(is_private=True)
    flanes_publicos = Flan.objects.filter(is_private=False)

    contexto = {
        "flanes": flanes,
        "flanes_privados": flanes_privados,
        "flanes_publicos": flanes_publicos,
    }
    return render(request, "index.html", contexto)


def about(request):
    return render(request, "about.html", {})


def welcome(request):
    flanes_privados = Flan.objects.filter(is_private=True)

    contexto = {
        "flanes_privados": flanes_privados,
    }
    return render(request, "welcome.html", contexto)


def registro_exitoso(request):
    return render(request, "registro_exitoso.html", {})


def contacto(request):
    if request.method == "POST":
        form = ContactFormForm(request.POST)
        if form.is_valid():
            contact_form = ContactForm.objects.create(**form.cleaned_data)
            return HttpResponseRedirect("/registro_exitoso")
    else:
        form = ContactFormForm()

    return render(request, "contacto.html", {"form": form})
