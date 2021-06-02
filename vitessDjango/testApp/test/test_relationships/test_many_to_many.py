#  Django's guide on Model layer
#  https://docs.djangoproject.com/en/3.2/topics/db/models/#relationships
#  https://docs.djangoproject.com/en/3.2/topics/db/examples/many_to_many/

from django.test import TestCase
from testApp.models import Book, Author
from datetime import date

class TestManyToMany(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test_book = Book.objects.create(title="TEST BOOK")
        cls.test_author_1 = Author.objects.create(first_name="John", last_name="Doe")
        cls.test_author_2 = Author.objects.create(first_name="Jane", last_name="Doe")
        cls.test_author_3 = Author.objects.create(first_name="Jack", last_name="Sparrow")
    
    def test_many_to_many(self):
        
        self.test_book.authors.set([self.test_author_1.pk, self.test_author_2.pk])
        self.assertEqual(
            self.test_book.authors.count(),
            2
        )

        self.test_author_3.book_set.add(self.test_book)
        self.assertEqual(
            self.test_book.authors.count(),
            3
        )