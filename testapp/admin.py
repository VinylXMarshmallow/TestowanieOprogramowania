from django.contrib import admin

from testapp.models import ListCars
from .models import Book
# Register your models here.
admin.site.register (Book)
admin.site.register(ListCars)