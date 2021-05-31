#  Django's guide on Model layer
#  https://docs.djangoproject.com/en/3.2/topics/db/models

from django.test import TestCase
from testApp.models import Person
from django.core.files.uploadedfile import SimpleUploadedFile


class CrudTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        small_gif = (
                b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x00\x00\x00\x21\xf9\x04'
                b'\x01\x0a\x00\x01\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02'
                b'\x02\x4c\x01\x00\x3b'
                )
        cls.test_image = SimpleUploadedFile('small.gif', small_gif, content_type='image/gif')
    