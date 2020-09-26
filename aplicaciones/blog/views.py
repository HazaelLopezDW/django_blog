from django.shortcuts import render
from .models import Post,Categoria
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator

def Home(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(estado = True)
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset)
        ).distinct()

    paginator = Paginator(posts,2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'index.html', {'posts': posts})

def DetallePost(request, slug):
    post = get_object_or_404(Post,slug = slug)
    return render(request, 'post.html',{'detalle_post':post})

def Generales(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(
        estado = True,
        categoria = Categoria.objects.get(nombre__iexact = 'General')
    )
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset),
            estado = True,
            categoria = Categoria.objects.get(nombre__iexact = 'General'),
        ).distinct()

    paginator = Paginator(posts,2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'generales.html',{'posts':posts})

def Programacion(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(
        estado = True,
        categoria = Categoria.objects.get(nombre__iexact = 'Programacion')
    )
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset),
            estado = True,
            categoria = Categoria.objects.get(nombre__iexact = 'Programacion')
        ).distinct()

    paginator = Paginator(posts,2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'programacion.html', {'posts':posts})

def Videojuegos(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(
        estado = True,
        categoria = Categoria.objects.get(nombre__iexact = 'VideoJuegos')
    )
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset),
            estado = True,
            categoria = Categoria.objects.get(nombre__iexact = 'VideoJuegos')
        ).distinct()

    paginator = Paginator(posts,2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'videojuegos.html', {'posts':posts})

def Tecnologia(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(
        estado = True,
        categoria = Categoria.objects.get(nombre__iexact = 'Tecnologia')
    )
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset),
            estado = True,
            categoria = Categoria.objects.get(nombre__iexact = 'Tecnologia')
        ).distinct()

    paginator = Paginator(posts,2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'tecnologia.html', {'posts':posts})

def Tutoriales(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(
        estado = True,
        categoria = Categoria.objects.get(nombre__iexact = 'Tutoriales')
    )
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset),
            estado = True,
            categoria = Categoria.objects.get(nombre__iexact = 'Tutoriales')
        ).distinct()

    paginator = Paginator(posts,2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'tutoriales.html', {'posts':posts})
