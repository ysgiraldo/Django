'''URL patterns allow you to map URLs to views. A URL pattern is composed of a string pattern, a view, 
and, optionally, a name that allows you to name the URL project-wide. Django runs through each URL 
pattern  and  stops  at  the  first  one  that  matches  the  requested  URL. Then,  Django  imports  the  view  
of the matching URL pattern and executes it, passing an instance of the HttpRequest class and the 
keyword or positional arguments.'''

from django.urls import path
from . import views


app_name = 'blog'
urlpatterns = [
    # post views
    # https://localhost:8000/blog/ # esta url va a caer en esta condicion
    path('', views.post_list, name='post_list'), 
    # https://localhost:8000/blog/7 # detalle del post con id 7
    path('<int:id>/', views.post_detail, name='post_detail'), 
]


'''In the preceding code, you define an application namespace with the app_name variable. This allows 
you to organize URLs by application and use the name when referring to them. You define two different 
patterns using the path() function. The first URL pattern doesn’t take any arguments and is mapped 
to the post_list view. The second pattern is mapped to the post_detail view and takes only one 
argument id, which matches an integer, set by the path converter int.'''