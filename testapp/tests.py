from django.test import TestCase
from django.urls import reverse
from testapp.models import Book
from testapp.models import Music

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

    def test_get_absolute_url(self):
         # Metoda test_get_absolute_url sprawdza, czy metoda get_absolute_url generuje poprawny URL.
         book = Book.objects.get(title="Test Book")
         self.assertEqual(book.get_absolute_url(), reverse('book-detail', kwargs={ 'pk': book.pk}))  # Sprawdzamy, czy URL do szczegółów książki jest poprawny.

    def test_available_default(self):
        book = Book.objects.get(title="Test Book")
        self.assertTrue(book.available)

    def test_reserve_method(self):

        book = Book.objects.get(title="Test Book")
        book.reserve()
        self.assertFalse(book.available)

    def test_is_new_release(self):

        new_release_book = Book.objects.get(title="Test Book")
        self.assertTrue(new_release_book.is_new_release)
        not_new_release_book = Book




class MusicModelTest(TestCase):
    def setUp(self):
        Music.objects.create(title="Bohemian Rhapsody", author="Queen", genre="Rock", popular=100)
        Music.objects.create(title="Shape of You", author="Ed Sheeran", genre="Pop", popular=200)

    def test_str_representation(self):
        bohemian_rhapsody = Music.objects.get(title="Bohemian Rhapsody")
        shape_of_you = Music.objects.get(title="Shape of You")

        self.assertEqual(str(bohemian_rhapsody), "Bohemian Rhapsody")
        self.assertEqual(str(shape_of_you), "Shape of You")

    def test_is_popular(self):
        bohemian_rhapsody = Music.objects.get(title="Bohemian Rhapsody")
        shape_of_you = Music.objects.get(title="Shape of You")
        self.assertTrue(bohemian_rhapsody.popular > 0)
        self.assertTrue(shape_of_you.popular > 0)



    def test_default_title(self):
        # Tworzymy obiekt Music bez podania tytułu
        music = Music.objects.create(author="Queen", genre="Rock", popular=100)

        # Sprawdzamy, czy domyślna wartość pola title została ustawiona poprawnie
        self.assertEqual(music.title, '')