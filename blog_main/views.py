from django.shortcuts import render
from blog.models import Blog

def index(request):
    blogs = Blog.objects.filter(status="Published").order_by('-created_at')
    context ={
        'blogs': blogs
    }
    return render(request, 'index.html', context)
