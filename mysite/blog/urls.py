'''URL patterns allow you to map URLs to views. A URL pattern is composed of a string pattern, a view, 
and, optionally, a name that allows you to name the URL project-wide. Django runs through each URL 
pattern  and  stops  at  the  first  one  that  matches  the  requested  URL. Then,  Django  imports  the  view  
of the matching URL pattern and executes it, passing an instance of the HttpRequest class and the 
keyword or positional arguments.'''

from django.urls import path
from . import views
from .feeds import LatestPostsFeed


app_name = 'blog'

urlpatterns = [
    # post views
    # https://localhost:8000/blog/ # esta url va a caer en esta condicion
    path('', views.post_list, name='post_list'),
    # path('', views.PostListView.as_view(), name='post_list'), 
    path('tag/<slug:tag_slug>/', views.post_list, name='post_list_by_tag'),
    # https://localhost:8000/blog/7 # detalle del post con id 7
    # path('<int:id>/', views.post_detail, name='post_detail'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
    path('<int:post_id>/share/', views.post_share, name='post_share'),
    path('<int:post_id>/comment/', views.post_comment, name='post_comment'),
    path('feed/', LatestPostsFeed(), name='post_feed'),
    path('search/', views.post_search, name='post_search'),
]