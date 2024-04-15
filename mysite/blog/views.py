from django.shortcuts import render
from .models import Post
from django.http import Http404, get_object_or_404

# Create your views here.

# A Django view is just a Python function that receives a web request and returns a web response. All 
# the logic to return the desired response goes inside the view.
# First, you will create your application views, then you will define a URL pattern for each view, and 
# finally,  you  will  create  HTML  templates  to  render  the  data  generated  by  the  views.  Each  view  will  
# render a template, passing variables to it, and will return an HTTP response with the rendered output.


def post_list(request):
    posts = Post.published.all()
    return render(request,
                 'blog/post/list.html',
                 {'posts': posts})

"""
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
"""

# Let’s create a second view to display a single post. Detalle de un post en particular

# def post_detail(request, id):
#     try:
#         post = Post.published.get(id=id)
#     except Post.DoesNotExist:
#         raise Http404("No Post found.")
#     return render(request,
#                   'blog/post/detail.html',
#                   {'post': post})

# Codigo resumido, evita definir try except

def post_detail(request, id):
    post = get_object_or_404(Post,
                             id=id,
                             status=Post.Status.PUBLISHED)
    return render(request,
                  'blog/post/detail.html',
                  {'post': post})