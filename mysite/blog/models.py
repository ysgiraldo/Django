from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()\
                     .filter(status=Post.Status.PUBLISHED)

class Post(models.Model):
    
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'
    
    title = models.CharField(max_length = 250)
    slug = models.SlugField(max_length = 250,
                            unique_for_date = 'publish') # friendly URL
    author = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default = timezone.now)
    # created y updated son campos que se actualizan automáticamente cuando se crea o modifica un registro
    # create tomara la fecha y hora actual cuando se cree un registro
    created = models.DateTimeField(auto_now_add = True)
    # updated tomara la fecha y hora actual cuando se modifique un registro
    updated = models.DateTimeField(auto_now = True)
    # 
    status = models.CharField(max_length = 2,
                            choices = Status.choices,
                            default = Status.DRAFT)
    objects = models.Manager() # The default manager.
    published = PublishedManager() # Our custom manager.
    
    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish']),
        ]
    
    def __str__(self):
        return self.title
    # The reverse() function will build the URL dynamically using the URL name defined in the URL patterns.
    
    def get_absolute_url(self):
        return reverse('blog:post_detail',
                       args=[self.publish.year,
                             self.publish.month,
                             self.publish.day,
                             self.slug])