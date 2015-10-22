from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.conf.urls import *




urlpatterns = [
    # Examples:
    url(r'^$', 'newsletter.views.home', name='home'),
    url(r'^contact/$', 'newsletter.views.contact', name='contact'),
    url(r'^about/$', 'trydjango18.views.about', name='about'),

    

    url(r'^comments/', include('django_comments.urls')),
    

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
   
	url(r'^blog/', include('blog.urls')),
    url(r'^portfolio/', include('portfolio.urls')),
    url(r'^user/', include('user_profile.urls')),

    url(r'^chat/', include('djangoChat.urls')), 
    

   
]
   


if not settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  