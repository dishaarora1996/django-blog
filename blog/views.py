from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Blog
from blog.forms import BlogPostForm
from django.template.defaultfilters import slugify
from django.contrib import messages

# Create your views here.

@login_required(login_url='login_user')
def dashboard(request):
    blogs = Blog.objects.filter(author = request.user)
    context ={
        'blogs': blogs
    }
    return render(request, 'dashboard.html', context)



def single_blog(request, blog_slug):
    single_blog = get_object_or_404(Blog, slug=blog_slug)
    context ={"single_blog": single_blog}
    return render(request, 'single-blog.html', context)

@login_required(login_url='login_user')
def add_blog(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            post.slug = f'{slugify(post.title)}-{post.id}'
            post.save()
            return redirect('dashboard')
        else:
            messages.error(request, f"Error: {form.errors}")

    form = BlogPostForm()
    context ={
        'form': form
    }
    return render(request, 'add-blog.html', context)


@login_required(login_url='login_user')
def edit_blog(request, blog_slug):

    blog = get_object_or_404(Blog, slug=blog_slug)

    if blog.author != request.user:
        messages.error(request, f"You do not have permission to edit this blog")
        return redirect('dashboard')

    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            post = form.save()
            post.slug = f'{slugify(post.title)}-{post.id}'
            post.save()
            messages.success(request, 'Blog updated successfully')
            return redirect('dashboard')

    form = BlogPostForm(instance=blog)
    context ={
        'form': form,
        'blog': blog
    }
    return render(request, 'edit-blog.html', context)

@login_required(login_url='login_user')
def delete_blog(request, blog_slug):
    blog = get_object_or_404(Blog, slug=blog_slug)

    if blog.author != request.user:
        messages.error(request, f"You do not have permission to delete this blog")
        return redirect('dashboard')

    blog.delete()

    return redirect('dashboard')
