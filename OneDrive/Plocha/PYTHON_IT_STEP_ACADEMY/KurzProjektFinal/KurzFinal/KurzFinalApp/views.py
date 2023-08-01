from django.shortcuts import render
from django.http import HttpResponse
from .models import dog_pictures # tečku dáváme, když to implementujeme z lokálního modulu -> tečka = hledej něco ve složce ve které jsem
from django.shortcuts import get_object_or_404

def detail(request, dog_id):
    dog = get_object_or_404(dog_pictures,pk=dog_id)
    return render(request, 'detail.html', {'dog':dog})

def home(request):
    # searchTerm = request.GET.get('searchPicture')
    return render(
        request=request,
        template_name='home.html',
        )

def kontakty(request):
    email = request.GET.get('email')

    return render(

        request,
        'kontakty.html',
        # template_name='email.html',
        context = {'email' : email}
    )

def signup(request):
    email = request.GET.get('email')

    return render(
        request=request,
        template_name='email.html',
        context = {'email' : email}
    )

def galerie(request):
    searchPicture = request.GET.get('searchPicture')
    if searchPicture:
        pictures = dog_pictures.objects.filter(title__icontains=searchPicture)
    else:
        pictures = dog_pictures.objects.all() 
    return render(request, 'galerie.html',{'searchPicture': searchPicture, 'pictures': pictures})