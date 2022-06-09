from django.db import models
from django.utils import timezone
# Create your models here.

class Photo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey('Categories', on_delete=models.CASCADE, default=1)
    location = models.ForeignKey('Locations', on_delete=models.CASCADE, default=1)


    def __str__(self):
        return self.title

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def update_image(self):
        self.update()

    @classmethod
    def get_all(cls):
        photos = cls.objects.all()
        return photos

    @classmethod
    def search_by_category(cls, search_term):
        photos = cls.objects.filter(category__name__icontains=search_term)
        return photos

    @classmethod
    def filter_by_location(cls, location):
        photos = Photo.objects.filter(location__city__icontains=location)
        return photos



class Categories(models.Model):
    '''
    model to handle categories
    '''
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    @classmethod
    def get_all(cls):
        categories = Categories.objects.all()
        return categories

    @classmethod
    def search_by_category(cls, search_term):
        categories = Categories.objects.filter(name__icontains=search_term)
        return categories


class Locations(models.Model):
    '''
    model to handle locations
    '''
    city = models.CharField(max_length=30)
    country = models.CharField(max_length=30)

    def __str__(self):
        return self.city

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    @classmethod
    def update_location(cls, search_term,location):

        try:
            to_update = Locations.objects.get(city=search_term)
            to_update.city = location
            to_update.save()
            return to_update
        except Locations.DoesNotExist:
            print('Location does not exist')


    @classmethod
    def get_all(cls):
        locations = Locations.objects.all()
        return locations
    
    @classmethod
    def filter_by_location(cls, search_term):
        locations = Locations.objects.filter(city__icontains=search_term)
        return locations
    
    @classmethod
    def search_by_country(cls, search_term):
        locations = Locations.objects.filter(country__icontains=search_term)
        return locations
    
    @classmethod
    def search_by_city(cls, search_term):
        locations = Locations.objects.filter(city__icontains=search_term)
        return locations
