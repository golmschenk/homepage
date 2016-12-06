"""
Tests for the views.
"""

from django.test import TestCase


class TestHomeView(TestCase):

    def test_front_page_renders_home_template(self):
        response = self.client.get('/climate-change')
        self.assertTemplateUsed(response, 'climatechange/home.html')
