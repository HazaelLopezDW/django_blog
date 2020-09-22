from django.urls import path
from .views import Home,Generales

urlpatterns = [
    path('', Home, name = 'index'),
    path('generales/', Generales, name = 'generales'),
]
