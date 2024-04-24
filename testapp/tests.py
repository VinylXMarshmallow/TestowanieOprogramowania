from django.test import TestCase
from django.urls import reverse
from testapp.models import Book

from datetime import datetime, timedelta

# Create your tests here.

class BookModelTest(TestCase):
    def setUp(self):
        Book.objects.create(title='Test Book', author='Author Name', borrow_count= 101, publish_date=datetime.now().date() - timedelta(30))
        Book.objects.create (title='Test Title', author='Test Name', borrow_count= 50, publish_date=datetime.now().date() - timedelta(800))




    def test_is_popular(self):
        popular_book = Book.objects.get(title='Test Book')
        not_popular_book= Book.objects.get(title='Test Title')

        self.assertTrue(popular_book.is_popular())
        self.assertFalse(not_popular_book.is_popular())

    def test_book_creation(self):
        book = Book.objects.get(title="Test Book")
        self.assertEqual(book.author, "Author Name")
        self.assertEqual(book.borrow_count,101)

    def test_genre(self):
        book = Book.objects.get(title="Test Book")
        book.genre = "Fantasy"
        book.save()
        self.assertEqual(book.genre,"Fantasy")
    def test_string_representation(self):
        book = Book.objects.get(title="Test Book")
        self.assertEqual(book.string_representation(),"Test Book by Author Name")


