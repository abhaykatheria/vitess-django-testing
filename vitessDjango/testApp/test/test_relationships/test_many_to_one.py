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

        cls.test_article_1 = Article.objects.create(
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

    def test_value_error(self):
        # an object must be saved before it can be assigned to a foreign key relationship
        reporter_2 = Reporter(first_name="Jane", last_name="Doe", email="jane@doe.com")
        try:
            test_article_3 = Article.objects.create(
                headline = 'TEST NEWS 3',
                pub_date = date(2020,3,1),
                reporter = reporter_2
            )
        except ValueError as ve:
            pass

    def test_type_error(self):
        try:
            reporter_2 = Reporter.objects.create(first_name="Jane", last_name="Doe", email="jane@doe.com")
            self.reporter_1.article_set.add(reporter_2)
        except TypeError:
            pass
    
    def test_article_creation_by_reporter_object(self):
        # articles can be created by using reporter objects also
        test_article_3 = self.reporter_1.article_set.create(
            headline = 'TEST NEWS 3',
            pub_date = date(2020,3,1),
        )

        self.assertEqual(
            test_article_3.reporter,
            self.reporter_1
        )

    def test_changing_foreign_key_of_existing_article(self):
        # articles can be moved from one article_set to another
        reporter_2 = Reporter.objects.create(first_name="Jane", last_name="Doe", email="jane@doe.com")
        reporter_2.article_set.add(self.test_article_1)

        self.assertEqual(
            self.test_article_1.reporter,
            reporter_2
        )

    def test_queries(self):
        # Find all Articles for any Reporter whose first name is "John".
        article_query_set = Article.objects.filter(reporter__first_name='John')
        self.assertEqual(len(article_query_set), 2)

        # querying with multiple fields 
        article_query_set = Article.objects.filter(reporter__first_name='John', reporter__last_name='Doe')
        self.assertEqual(len(article_query_set), 2)

        # For the related lookup you can supply a primary key value or pass the related object explicitly
        article_query_set = Article.objects.filter(reporter__pk=1)
        self.assertEqual(len(article_query_set), 2)
        article_query_set = Article.objects.filter(reporter = self.reporter_1)
        self.assertEqual(len(article_query_set), 2)

        reporter_2 = Reporter.objects.create(first_name="Jane", last_name="Doe", email="jane@doe.com")
        test_article_3 = Article.objects.create(
                headline = 'TEST NEWS 3',
                pub_date = date(2020,3,1),
                reporter = reporter_2
            )
        # we can pass multiple primary_key to filter objects
        article_query_set = Article.objects.filter(reporter__in=[1,2]).distinct()
        self.assertEqual(len(article_query_set), 3)

        # using queryset instead of a literal list of instances
        article_query_set = Article.objects.filter(reporter__in=Reporter.objects.filter(first_name='John')).distinct()
        self.assertEqual(len(article_query_set), 2)

        # Querying in the opposite direction
        reporter_set = Reporter.objects.filter(article__pk=1)
        self.assertEqual(len(reporter_set), 1)
        
        reporter_set = Reporter.objects.filter(article__headline__startswith='TEST')
        self.assertEqual(len(reporter_set), 3)

        reporter_set = Reporter.objects.filter(article__headline__startswith='TEST').distinct()
        self.assertEqual(len(reporter_set), 2)

    def test_delete_query(self):
        # If you delete a reporter, their articles will be deleted if on_delete is is set to cascade which is default
        article_query_set = Article.objects.all()
        self.assertEqual(len(article_query_set), 2)

        self.reporter_1.delete()

        article_query_set = Article.objects.all()
        self.assertEqual(len(article_query_set), 0)


