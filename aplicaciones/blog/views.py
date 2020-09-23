from django.shortcuts import render
from .models import Post,Categoria
from django.shortcuts import get_object_or_404

def Home(request):
    posts = Post.objects.filter(estado = True)
    return render(request, 'index.html', {'posts': posts})

def DetallePost(request, slug):
    post = get_object_or_404(Post,slug = slug)
    return render(request, 'post.html',{'detalle_post':post})

def Generales(request):
    posts = Post.objects.filter(
        estado = True,
        categoria = Categoria.objects.get(nombre__iexact = 'General')
    )
    return render(request, 'generales.html',{'posts':posts})

def Programacion(request):
    posts = Post.objects.filter(
        estado = True,
        categoria = Categoria.objects.get(nombre__iexact = 'Programacion')
    )
    return render(request, 'programacion.html', {'posts':posts})

def Videojuegos(request):
    posts = Post.objects.filter(
        estado = True,
        categoria = Categoria.objects.get(nombre__iexact = 'VideoJuegos')
    )
    return render(request, 'videojuegos.html', {'posts':posts})

def Tecnologia(request):
    posts = Post.objects.filter(
        estado = True,
        categoria = Categoria.objects.get(nombre__iexact = 'Tecnologia')
    )
    return render(request, 'tecnologia.html', {'posts':posts})

def Tutoriales(request):
    posts = Post.objects.filter(
        estado = True,
        categoria = Categoria.objects.get(nombre__iexact = 'Tutoriales')
    )
    return render(request, 'tutoriales.html', {'posts':posts})
