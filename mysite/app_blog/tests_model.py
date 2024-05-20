from django.test import TestCase
from app_blog import models

class CategoryModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test
        models.Category.objects.create(category='Innovations', slug='innovations')

    def test_get_absolute_url(self):
        category=models.Category.objects.get(id=1)
        self.assertEquals(category.get_absolute_url(), '/articles/category/innovations')
