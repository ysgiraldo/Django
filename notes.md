La arquitectura de Django sigue el patrón de diseño Modelo-Vista-Controlador (MVC). En Django, el modelo representa los datos y la lógica de negocio, la vista maneja la presentación de los datos al usuario y el controlador maneja las interacciones del usuario y coordina el flujo de datos entre el modelo y la vista.

Django sigue el patrón de diseño Modelo-Vista-Controlador (MVC), pero en la comunidad de Django a menudo se refiere a esto como Modelo-Vista-Template (MVT) debido a la forma en que se manejan las responsabilidades. Aquí está el desglose:

1. Modelo (Model): El modelo es la representación de la base de datos. Define la estructura de la base de datos, incluyendo tablas, campos, relaciones, etc. Django automáticamente genera la base de datos basándose en los modelos definidos.

2. Vista (View): En Django, la vista es donde se procesan las solicitudes HTTP y se prepara la respuesta HTTP. Las vistas toman una solicitud web y devuelven una respuesta web. Las vistas en Django son más similares a los controladores en el patrón MVC tradicional.

3. Plantilla (Template): Las plantillas son la parte que se encarga de la presentación en Django. Son archivos HTML que pueden contener lógica de presentación, como bucles y condicionales, para insertar datos dinámicamente en la página web.

4. URL Dispatcher: Django utiliza un despachador de URL para dirigir las solicitudes HTTP a la vista correcta basándose en la URL de la solicitud.

5. Middlewares: Los middlewares en Django son componentes que se ejecutan antes de que la vista procese la solicitud y después de que la vista haya terminado de procesar la solicitud. Pueden ser utilizados para realizar tareas como la manipulación de solicitudes y respuestas, la autenticación, la autorización, etc.

6. ORM (Object-Relational Mapping): Django viene con un ORM incorporado que facilita la interacción con la base de datos. El ORM de Django permite interactuar con la base de datos, como si fueran objetos Python.

Esta arquitectura permite un desarrollo rápido y limpio, manteniendo las diferentes responsabilidades bien separadas.

Let’s look at what startproject created:

These files are:

* The outer mysite/ root directory is a container for your project. Its name doesn’t matter to Django; you can rename it to anything you like.
* manage.py: A command-line utility that lets you interact with this Django project in various ways. You can read all the details about manage.py in [django-admin and manage.py.](https://docs.djangoproject.com/en/5.0/ref/django-admin/)
* The inner mysite/ directory is the actual Python package for your project. Its name is the Python package name you’ll need to use to import anything inside it (e.g. mysite.urls).
* mysite/__init__.py: An empty file that tells Python that this directory should be considered a Python package. If you’re a Python beginner, [read more about packages in the official Python docs.](https://docs.python.org/3/tutorial/modules.html#tut-packages)
* mysite/settings.py: Settings/configuration for this Django project. [Django settings](https://docs.djangoproject.com/en/5.0/topics/settings/) will tell you all about how settings work.
* mysite/urls.py: The URL declarations for this Django project; a “table of contents” of your Django-powered site. [You can read more about URLs in URL dispatcher.](https://docs.djangoproject.com/en/5.0/topics/http/urls/)
* mysite/asgi.py: An entry-point for ASGI-compatible web servers to serve your project. [See How to deploy with ASGI](https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/) for more details.
* mysite/wsgi.py: An entry-point for WSGI-compatible web servers to serve your project. [See How to deploy with WSGI for more details.](https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/)


The preceding structure will be the file structure for your templates. The base.html file will include 
the  main  HTML  structure  of  the  website  and  divide  the  content  into  the  main  content  area  and  a  
sidebar. The list.html and detail.html files will inherit from the base.html file to render the blog 
post list and detail views, respectively.
Django has a powerful template language that allows you to specify how data is displayed. It is based 
on template tags, template variables, and template filters:
• Template tags control the rendering of the template and look like {% tag %}
• Template variables get replaced with values when the template is rendered and look like {{ 
variable }}
• Template filters allow you to modify variables for display and look like {{ variable|filter }}
You can see all built-in template tags and filters at https://docs.djangoproject.com/en/4.1/ref/
templates/builtins/.



* Always use the {% url %} template tag to build URLs in your templates instead of writing 
hardcoded URLs. This will make your URLs more maintainable.




    The {% load static %} template tag loads the static template tag library, 
    which is included in Django by default. 
    This library provides the {% static %} template tag, 
    which generates the absolute URL of static files.
Va a evitar la carga de elementos estáticos, como css para que se pueda renderizar de una mejor manera

{% block title %}{% endblock %} 
    Define un bloque llamado title. 
    Los bloques son áreas de un template que los hijos pueden sobrescribir. 
    En este caso, el bloque title se utiliza para proporcionar un título para la página.
    las paginas internas como detail y list puedan sobreescribir esos elementos

{% block content %}{% endblock %} 
    Define un bloque llamado content. 
    Este bloque se utiliza para proporcionar el contenido de la página.
    las paginas internas como detail y list puedan sobreescribir esos elementos


 
With the {% extends %} template tag, you tell Django to inherit from the blog/base.html template. 
Then, you fill the title and content blocks of the base template with content. You iterate through 
the posts and display their title, date, author, and body, including a link in the title to the detail URL 
of the post. We build the URL using the {% url %} template tag provided by Django.

This template tag allows you to build URLs dynamically by their name. We use blog:post_detail to 
refer to the post_detail URL in the blog namespace. We pass the required post.id parameter to 
build the URL for each post.


# Views - blog
A Django view is just a Python function that receives a web request and returns a web response. All 
the logic to return the desired response goes inside the view.
First, you will create your application views, then you will define a URL pattern for each view, and 
finally,  you  will  create  HTML  templates  to  render  the  data  generated  by  the  views.  Each  view  will  
render a template, passing variables to it, and will return an HTTP response with the rendered output.

This is our very first Django view. The post_list view takes the request object as the only parameter. 
This parameter is required by all views.
In this view, we retrieve all the posts with the PUBLISHED status using the published manager that we 
created previously.
Finally, we use the render() shortcut provided by Django to render the list of posts with the given 
template. This function takes the request object, the template path, and the context variables to render 
the given template. It returns an HttpResponse object with the rendered text (normally HTML code).
The  render()  shortcut  takes  the  request  context  into  account,  so  any  variable  set  by  the  template  
context processors is accessible by the given template. Template context processors are just callables 
that set variables into the context. You will learn how to use context processors in Chapter 4, Building 
a Social Website.


# Admin
When you register a model in the Django administration site, you get a user-friendly 
interface generated by introspecting your models that allows you to list, edit, create, and 
delete objects in a simple way
esta es la forma de registro facil de un modelo en el admin de Django
admin.site.register(Post)
Una forma mas customizada de registrar un modelo en el admin de Django
from django.contrib import admin
from .models import Post
los decoradores son una forma en la cual tu añades funcionalidades adicionales 
a una funcion o clase sin modificar su estructura (cuerpo de la funcion o clase)


# Urls - blog
In the preceding code, you define an application namespace with the app_name variable. This allows 
you to organize URLs by application and use the name when referring to them. You define two different 
patterns using the path() function. The first URL pattern doesn’t take any arguments and is mapped 
to the post_list view. The second pattern is mapped to the post_detail view and takes only one 
argument id, which matches an integer, set by the path converter int.