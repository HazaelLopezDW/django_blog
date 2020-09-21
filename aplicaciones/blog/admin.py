from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin 

class CategoriaAdmin(admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ('nombre','estado','fecha_creacion',)

class AutorAdmin(admin.ModelAdmin):
    search_fields = ['nombres','apellidos','correo']
    list_display = ('nombres','apellidos','correo','estado','fecha_creacion',)

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Autor, AutorAdmin)
