from django.contrib import admin
from .models import Category, Blog
# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'Category', 'author','status','is_featured')
    search_fields=('title','id','status')
admin.site.register(Category)
admin.site.register(Blog, BlogAdmin) 