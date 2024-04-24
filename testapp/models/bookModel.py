from django.db import  models
from django.urls import  reverse
from datetime import datetime,timedelta
from datetime import date

class Book(models.Model):

    title = models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    genre=models.CharField(max_length=100,  blank=True)
    borrow_count = models.IntegerField(default=0)
    publish_date=models.DateField(default=date.today)
    available=models.BooleanField(default=True)

    def __str__(self):
        return self.title

        # Definiujemy metody instancji modelu:

    def is_popular(self):
        """Zwraca True, jeśli książka została wypożyczona więcej niż 100 razy."""
        # Zwraca wartość logiczną True, jeśli liczba wypożyczeń przekracza 100.
        return self.borrow_count > 100

    @property
    def is_new_release(self):
        """Sprawdza, czy książka jest nowym wydaniem (wydana w ciągu ostatnich 2 lat)."""
        # Zwraca True, jeśli książka została wydana w ciągu ostatnich dwóch lat.
        return (datetime.now().date() - self.publish_date) <= timedelta(days=730)

    def string_representation(self):
        """Zwraca reprezentację stringową książki."""
        # Formatuje i zwraca tytuł i autora książki jako string.
        return f"{self.title} by {self.author}"

    def get_absolute_url(self):
        """Generuje URL do szczegółów książki."""
        # Używa funkcji reverse do wygenerowania URL na podstawie nazwy wzorca URL 'book-detail'
        # i klucza głównego (pk) książki.
        return reverse('book-detail', kwargs={'pk': self.pk})

    def reserve(self):
        """Rezerwuje książkę (zmienia dostępność na False)."""
        # Ustawia atrybut available na False, oznaczając, że książka jest zarezerwowana.
        self.available = False
        # Zapisuje zmianę stanu obiektu do bazy danych.
        self.save()
    def __str__(self):
        return self.bookList

    class Meta:
        db_table = 'bookModel'