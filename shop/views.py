from django.shortcuts import render
from django.http import HttpResponse




def home(request):
    return render(request, "shop/home.html")
def catalog(request):
   return render (request, "shop/catalog.html")
def about(request):
    return render (request, "shop/about.html")
# Create your views here.
