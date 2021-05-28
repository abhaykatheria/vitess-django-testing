from django.test import TestCase

class CrudTestCase(TestCase):
    def setup(self):
        print("initiating")
    def test_create(self):
       assert(1==2)