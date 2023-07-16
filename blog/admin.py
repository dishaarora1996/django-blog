from django.contrib import admin
from .models import Blog
# Register your models here.



class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields ={'slug': ('title',)}
    list_display = ['title','content', 'author', 'status',  'created_at']
    search_fields = ("title", "author", "content")
    list_filter=('created_at', 'updated_at', 'status')

admin.site.register(Blog, BlogAdmin)
