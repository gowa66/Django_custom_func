from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext

# Create your views here.
def about(request):


	return render(request, "about.html", {})


def custom_404(request):
	return render(request, "404.html")

def custom_400(request):
	return render(request, "400.html")

def custom_500(request):
	return render(request, "500.html")

def handler404(request):
    response = render_to_response('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response


def handler500(request):
    response = render_to_response('500.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response