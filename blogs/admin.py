from django.contrib import admin
from .models import Category, Blog
# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'Category', 'author','is_featured')
admin.site.register(Category)
admin.site.register(Blog, BlogAdmin) 