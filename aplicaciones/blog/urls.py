from django.urls import path
from .views import *

urlpatterns = [
    path('', Home, name = 'index'),
    path('generales/', Generales, name = 'generales'),
    path('programacion/', Programacion, name = 'programacion'),
    path('videojuegos/', Videojuegos, name = 'videojuegos'),
    path('tecnologia/', Tecnologia, name = 'tecnologia'),
    path('tutoriales/', Tutoriales, name = 'tutoriales'),
    path('<slug:slug>/', DetallePost, name = 'detalle_post'),
]
