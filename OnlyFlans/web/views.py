from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import ContactForm, Flan
from .forms import ContactFormForm
from django.contrib.auth import login
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse



def index(request):
    flanes_publicos = Flan.objects.filter(is_private=False)

    contexto = {
        "flanes_publicos": flanes_publicos,
    }
    return render(request, "index.html", contexto)


def about(request):
    return render(request, "about.html", {})


@login_required
def welcome(request):
    flanes_privados = Flan.objects.filter(is_private=True)

    contexto = {
        "flanes_privados": flanes_privados,
    }
    return render(request, "welcome.html", contexto)


def registro_exitoso(request):
    return render(request, "usuario_existente.html", {})


def contacto(request):
    if request.method == "POST":
        form = ContactFormForm(request.POST)
        if form.is_valid():
            contact_form = ContactForm.objects.create(**form.cleaned_data)
            return HttpResponseRedirect("/registro_exitoso")
    else:
        form = ContactFormForm()

    return render(request, "contacto.html", {"form": form})

def usuario_existente(request):
    return render(request, "usuario_existente.html", {})

def sign_up(request):
    if request.method == "GET":
        form = UserCreationForm()
        return render(request, "signup.html", {"form": form})
    else:
        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    username=request.POST["username"],
                    password=request.POST["password1"],
                )
                user.save()
                login(request, user)
                return redirect("index")
                return HttpResponse("Usuario creado satisfactoriamente")
            except:
                return redirect("usuario_existente")
        return HttpResponse("Las contraseñas no coinciden")

def log_in(request):
    if request.method == "GET":
        return render(request, "login.html", {"form": AuthenticationForm()})
    else:
        user = authenticate(
            request,
            username=request.POST["username"],
            password=request.POST["password"],
        )
        if user is None:
            return render(
                request,
                "login.html",
                {
                    "form": AuthenticationForm(),
                    "error": "El usuario o contraseñas son incorrectos",
                },
            )
        else:
            login(request, user)
            return redirect("index")


def log_out(request):
    logout(request)
    return redirect("index")
