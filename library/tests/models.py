from django.test import TestCase
from library.models import Author, Book


class TestModels(TestCase):
    def test_book_has_an_author(self):
        book = Book.objects.create(title="The man in the high castle")
        philip = Author.objects.create(first_name="Philip", last_name="K. Dick")
        juliana = Author.objects.create(first_name="Juliana", last_name="Crain")
        book.authors.set([philip.pk, juliana.pk])
        self.assertEqual(book.authors.count(), 2)