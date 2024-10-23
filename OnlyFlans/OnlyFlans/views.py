from django.shortcuts import render

#INDEX - Landing Page
def index(request):
    return render(request, "index.html", {})

def about(request):
    return render(request, "about.html", {})

def welcome(request):
    return render(request, "welcome.html", {})