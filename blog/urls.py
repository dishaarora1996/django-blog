from django.urls import path
from .views import *

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('post/<slug:blog_slug>/', single_blog, name='single_blog'),
    path('add_blog/', add_blog, name='add_blog'),
]