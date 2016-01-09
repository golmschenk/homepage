from django.test import TestCase


class TestHomeView(TestCase):

    def test_front_page_renders_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')
