from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.conf.urls import *




urlpatterns = [
    # Examples:
    url(r'^$', 'newsletter.views.home', name='home'),
    url(r'^contact/$', 'newsletter.views.contact', name='contact'),
    url(r'^about/$', 'trydjango18.views.about', name='about'),

    url(r'^privacy/$', 'trydjango18.views.privacy', name='privacy'),
    url(r'^terms/$', 'trydjango18.views.terms', name='terms'),


   
    

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^blog/', include('blog.urls')),

    
    url(r'^user/', include('user_profile.urls')),

    url(r'^chat/', include('djangoChat.urls')), 
    

   
]



if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
