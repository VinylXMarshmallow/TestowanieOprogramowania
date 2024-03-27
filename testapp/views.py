from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Book

def add_image(request):
    submitted=False
# Create your views here.
class BookDetailView(DetailView):
    model = Book
    template_name = 'testapp/book_detail.html'
    context_object_name = 'book'