# -*- coding: utf-8 -*-
from django.db import models
 
# from django.db import models
# from django.contrib import admin

class Post(models.Model):
    title = models.CharField(max_length=255) # zagolovok posta
    datetime = models.DateTimeField(u'Дата публикации') # data publikacii
    content = models.TextField(max_length=10000) # text posta

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/blog/%i/" % self.id



# class BlogPost(models.Model):   
#     title = models.CharField(max_length=150)
#     short_body = models.TextField()
#     body = models.TextField()
#     timestamp = models.DateTimeField()
#     logo = models.ImageField(upload_to="static/")
#     class Meta:
#         ordering = ("-timestamp",)

# class BlogPostAdmin(admin.ModelAdmin):   
#     list_display = ("id", "title", "timestamp")

# admin.site.register(BlogPost, BlogPostAdmin)