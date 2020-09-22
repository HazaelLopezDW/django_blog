from django.shortcuts import render

def Home(request):
    return render(request, 'index.html')

def Generales(request):
    return render(request, 'generales.html')

def Programacion(request):
    return render(request, 'programacion.html')

def Videojuegos(request):
    return render(request, 'videojuegos.html')

def Tecnologia(request):
    return render(request, 'tecnologia.html')

def Tutoriales(request):
    return render(request, 'tutoriales.html')
