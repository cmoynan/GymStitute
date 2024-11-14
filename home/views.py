from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')

def custom_404_view(request, exception):
    return render(request, 'errors/404.html', status=404)