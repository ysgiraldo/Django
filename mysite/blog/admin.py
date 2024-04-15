from django.contrib import admin
from .models import Post

# este modulo de admin se encarga de toda la administracion de la aplicacion de la que es parte

# Register your models here.

# When you register a model in the Django administration site, you get a user-friendly 
# interface generated by introspecting your models that allows you to list, edit, create, and 
# delete objects in a simple way

# esta es la forma de registro facil de un modelo en el admin de Django
# admin.site.register(Post)

# Una forma mas customizada de registrar un modelo en el admin de Django

# from django.contrib import admin
# from .models import Post

# los decoradores son una forma en la cual tu añades funcionalidades adicionales 
# a una funcion o clase sin modificar su estructura (cuerpo de la funcion o clase)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    # con la confg de prepopulated_fields, el campo slug se llenara automaticamente con el titulo
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')
