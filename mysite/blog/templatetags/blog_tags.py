from django import template
from ..models import Post

register = template.Library()
# this returns the number of posts published in the blog
@register.simple_tag
def total_posts():
    return Post.published.count()