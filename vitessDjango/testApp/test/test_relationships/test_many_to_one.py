#  Django's guide on Model layer
#  https://docs.djangoproject.com/en/3.2/topics/db/models/#relationships
#  https://docs.djangoproject.com/en/3.2/topics/db/examples/many_to_one/

from django.test import TestCase
from testApp.models import Reporter,Article
from datetime import date

class TestManyToOne(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.reporter_1 = Reporter.objects.create(first_name='John', last_name='Doe', email='john@doe.com')

        cls. test_article_1 = Article.objects.create(
            headline = 'TEST NEWS 1',
            pub_date = date(2020,2,1),
            reporter = cls.reporter_1
        )

        cls.test_article_2 = Article.objects.create(
            headline = 'TEST NEWS 2',
            pub_date = date(2020,2,2),
            reporter =cls. reporter_1
        )

    def test_many_to_one(self):
        
        self.assertEqual(
            str(self.test_article_1.reporter),
            "John Doe"
        )

        self.assertEqual(
            len(self.reporter_1.article_set.all()),
            2
        )
