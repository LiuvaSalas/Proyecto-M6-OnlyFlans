from django.shortcuts import render

#INDEX - Landing Page
def index(request):
    return render(request, "index.html", {})