from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Photo,Categories, Locations

# Create your views here.

def home(request):
    return render(request, 'home.html')

def display(request):
    pictures = Photo.get_all()
    locations = Locations.get_all()
    categories = Categories.get_all()
    return render(request, 'display.html', {'pictures': pictures, 'locations': locations, 'categories': categories})

def search(request):
    if 'category' in request.GET and request.GET['category']:
        search_term = request.GET.get('category')
        searched_category = Categories.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'search.html', {'message': message, 'category': searched_category})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html', {'message': message})
    
def location(request,citi):
    images = Photo.filter_by_location(citi)
    return render(request, 'location.html', {'locations': images})

def categories(request,category):
    images = Photo.search_by_category(category)
    return render(request, 'categories.html', {'categories': images})