python manage.py shell

from blog.models import Post
Post.objects.filter(title__search='django')

from django.contrib.postgres.search import SearchVector
from blog.models import Post
Post.objects.annotate(search=SearchVector('title', 'body')).filter(search='django')