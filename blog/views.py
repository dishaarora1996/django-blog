from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Blog
# Create your views here.



@login_required(login_url='login_user')
def dashboard(request):
    blogs = Blog.objects.filter(author = request.user)
    context ={
        'blogs': blogs
    }
    return render(request, 'dashboard.html', context)
