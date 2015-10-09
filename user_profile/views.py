from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
from user_profile.models import UserProfile
from forms import UserProfileForm
from django.shortcuts import redirect

@login_required
def update_profile(request):
	userProfile = UserProfile.objects.get(user=request.user)
	form = UserProfileForm(initial={'bio':userProfile.bio})
	return render_to_response('user_profile/update_profile.html', {'form':form}, RequestContext(request))

def profile(request, profile_id):
	if profile_id == "0":
		if request.user.is_authenticated:
			userProfile = UserProfile.objects.get(user=request.user)
	else:
		userProfile = UserProfile.objects.get(pk=profile_id)

	return render_to_response('user_profile/profile.html', {'userProfile':userProfile}, RequestContext(request))	

@login_required
def send_update_profile(request):
	if request.method == 'POST':
		form = UserProfileForm(request.POST)
		if form.is_valid():
			userProfile = UserProfile.objects.get(user=request.user)
			bio = form.cleaned_data['bio']
			userProfile.bio = bio
			userProfile.save()
			return redirect('/user/profile/' +str(userProfile.id))

	else:
		form = UserProfileForm()

	return redirect('/user/send_update_profile')