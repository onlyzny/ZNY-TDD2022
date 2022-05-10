from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest, response

from lists.views import home_page #(2)

class HomePageTest(TestCase):
    '''
    def test_root_url_resolves_to_home_page_view(self):
        found=resolve('/')
        self.assertEqual(found.func,home_page)

    def test_home_page_returns_correct_html(self):
        response = self.client.get('/') #1

        html=response.content.decode('utf8') #2
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>',html)
        self.assertTrue(html.endswith('</html>'))

        self.assertTemplateUsed(response, 'home.html') #3

    '''
    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response,'home.html')

    def test_can_save_a_POST_request(self):
        response = self.client.post('/', data={'item_text': 'A new list item'})
        self.assertIn('A new list item', response.content.decode())