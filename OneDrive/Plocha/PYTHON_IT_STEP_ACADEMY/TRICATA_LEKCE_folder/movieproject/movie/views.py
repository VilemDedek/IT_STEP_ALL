from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie # tečku dáváme, když to implementujeme z lokálního modulu -> tečka = hledej něco ve složce ve které jsem

# Create your views here.
# def home(request):
#     return HttpResponse('<h1>This is Home!</h1>')

def about(request):
    return HttpResponse('<h1>This is ABOUT!!</h1>')

context={'name': "Honza"}

def home(request):
    searchTerm = request.GET.get('searchMovie')
    return render(
        request=request,
        template_name='home.html',
        context = context
        )

def signup(request):
    email = request.GET.get('email')

    return render(
        request=request,
        template_name='email.html',
        context = {'email' : email}
    )

def home(request):
 searchTerm = request.GET.get('searchMovie')
 if searchTerm:
    movies = Movie.objects.filter(title__icontains=searchTerm)
 else:
     movies = Movie.objects.all() 
 return render(request, 'home.html',{'searchTerm':searchTerm, 'movies': movies})