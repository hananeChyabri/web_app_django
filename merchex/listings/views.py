from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Band
from listings.models import Listing


def band_list(request):
    bands = Band.objects.all()
    return render(request, 'listings/band_list.html',{'bands': bands})

def about(request):
     return render(request, 'listings/about.html')

def listing(request):
    listings = Listing.objects.all()
    return render(request, 'listings/listings.html',{'listings': listings})

def contact(request):
    return render(request, 'listings/contact.html')

def band_detail(request,id):
    band = Band.objects.get(id=id)
    return render(request,
                  'listings/band_detail.html',
                  {'band':band})
