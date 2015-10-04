# -*- coding: utf-8 -*-
from django.db import models
 


class Post(models.Model):
    title = models.CharField(max_length=255) # zagolovok posta
    datetime = models.DateTimeField(u'Дата публикации') # data publikacii
    content = models.TextField(max_length=10000) # text posta

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/blog/%i/" % self.id



