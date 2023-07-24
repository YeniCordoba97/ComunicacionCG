from django.shortcuts import render, HttpResponse

# Create your views here.
def Registro(request):
    return render(request, "core/Registro.html")

def home(request):
    return render(request, "core/home.html")