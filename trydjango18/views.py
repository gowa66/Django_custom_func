from django.shortcuts import render


# Create your views here.
def about(request):


	return render(request, "about.html", {})


def custom_404(request):
	return render(request, "404.html")

def custom_400(request):
	return render(request, "400.html")

def custom_500(request):
	return render(request, "500.html")

