from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
	#return HttpResponse("Hello, world. Yay! My first app is online.")
	return render( request, 'index.html')


