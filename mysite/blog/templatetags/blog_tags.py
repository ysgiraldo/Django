from django import template
from ..models import Post

register = template.Library()
# this returns the number of posts published in the blog
@register.simple_tag
def total_posts():
    return Post.published.count()

# this will display the latest posts in the sidebar
@register.inclusion_tag('blog/post/latest_posts.html')
def show_latest_posts(count=5):
    latest_posts = Post.published.order_by('-publish')[:count]
    return {'latest_posts': latest_posts}