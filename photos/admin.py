from django.contrib import admin
from .models import Photo,Categories, Locations

# Register your models here.

admin.site.register(Photo)
admin.site.register(Categories)
admin.site.register(Locations)
