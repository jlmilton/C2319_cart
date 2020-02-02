from django.test import SimpleTestCase
from django.urls import reverse, resolve
from home_page.views import home, about

class TestUrls(SimpleTestCase):

    def test_home_url(self):
        url = reverse('home-home') #home-home is from url
        self.assertEquals(resolve(url).func , home) #home is from views

    def test_about_url(self):
        url = reverse('home-about') #home-about from url
        self.assertEquals(resolve(url).func , about) #about is from views

# command : python3 manage.py test home_page/
