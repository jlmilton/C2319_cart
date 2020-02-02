from django.test import SimpleTestCase
from django.urls import reverse, resolve
from posts.views import add_post


class TestUrls(SimpleTestCase):

    def test_add_post(self):
        url = reverse('add_post')
        # print(resolve(url))
        self.assertEquals(resolve(url).func , add_post)

    # def test_edit_post(self):
    #     url = reverse('edit_post')
    #     print(resolve(url))

#command : python3 manage.py test posts
