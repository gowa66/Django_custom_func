from django.db.models import *
from django.contrib.auth.models import User
from django.contrib import admin
from django.core.mail import send_mail

from shared.utils import *

notify = False

class BlogPost(BaseModel):
    title   = CharField(max_length=60)
    body    = TextField()
    created = DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created"]

    def __unicode__(self):
        return self.title


class BlogComment(BaseModel):
    author  = CharField(max_length=60, blank=True)
    body    = TextField()
    post    = ForeignKey(BlogPost, related_name="comments",  blank=True, null=True)
    created = DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u"%s: %s" % (self.post, self.body[:60])

    
