from django.contrib import admin

from testapp.models import ListCars
from .models import Book
from .models import Music
# Register your models here.
admin.site.register (Book)
admin.site.register(ListCars)
admin.site.register(Music)