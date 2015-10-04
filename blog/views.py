# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.
from blog.models import Post 
from django.views.generic import ListView, DetailView

# from django.template import loader, Context 
# from django.http import HttpResponse 
# from blog.models import BlogPost

class PostsListView(ListView): # представление в виде списка
    model = Post                   # модель для представления 

class PostDetailView(DetailView): # детализированное представление модели
    model = Post



# def archive(request):   
#     posts = BlogPost.objects.all()   
#     t = loader.get_template("archive.html")   
#     c = Context({"posts": posts })   
#     return HttpResponse(t.render(c))    