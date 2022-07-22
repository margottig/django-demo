from django.shortcuts import render, redirect
from .models import Banda, Fan

# Create your views here.

def raiz(request):
    context={
        "bandas": Banda.objects.all()
    }

    return render(request, "index.html", context)

def crearBanda(request):
    if request.method == 'POST':
        nuevaBanda = Banda.objects.create(
            nombre = request.POST['nombre'],
            descripcion = request.POST['descripcion'],
            pais = request.POST['pais']
        )
        print(nuevaBanda)
    return redirect('/')

def crearFan(request):
    if request.method == 'POST':
        nuevoFan = Fan.objects.create(
            nombre = request.POST['nombreFan'],
        )
        print(nuevoFan)
    return redirect('/')

def showBanda(request, id_banda):
    context={
        "banda": Banda.objects.get(id=id_banda),
        "fans": Fan.objects.all()
    }
    return render(request, "showBanda.html", context)

def agregarFan(request, id_banda):
    banda = Banda.objects.get(id=id_banda)
    fan = Fan.objects.get(
        id = request.POST['agregarFan']
    )
    banda.fans.add(fan)
    return redirect(f'/showBand/{id_banda}')



