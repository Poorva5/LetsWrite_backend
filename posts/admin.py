from django.contrib import admin
from .models import Post, Category

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'published_on', 'status')
    prepopulated_fields = {'slug':('title',)}
    date_hierarchy = 'published_on'
    ordering = ('status', 'published_on')


@admin.register(Category)
class Comment(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug':('name',)}
