from django.conf.urls import *



urlpatterns = patterns('',
	url(r'^profile/(?P<profile_id>\d+)/$', 'user_profile.views.profile' ),
	url(r'^update_profile/$', 'user_profile.views.update_profile', name='update_profile'),
	url(r'^send_update_profile/$', 'user_profile.views.send_update_profile'),

	url(r'^profile/0', 'user_profile.views.profile', name='my_profile' ),

	)



