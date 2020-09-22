from django.shortcuts import render

def Home(request):
    return render(request, 'index.html')

def Generales(request):
    return render(request, 'generales.html')
