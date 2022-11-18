from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=250, db_index=True)
    slug = models.SlugField(unique=True)
    
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
     
    def __str__(self):
        return self.name

    
class Post(models.Model):

    class StatusChoice(models.TextChoices):
        DRAFT = "Draft"
        PUBLISHED = "Published"

    title = models.CharField(max_length=250)
    category = models.ForeignKey(Category, related_name='blog_category', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    image = models.ImageField(upload_to='post/%Y/%m/%d', null=True, blank=True)
    published_on = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100,choices=StatusChoice.choices, default=StatusChoice.DRAFT)
    slug = models.SlugField(max_length=250, unique=True)

    class Meta:
        ordering = ('-published_on', )

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug= '-'.join((slugify(self.title), slugify(self.author)))
        super(Post, self).save(*args, **kwargs)
