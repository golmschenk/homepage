"""
Tests to check that the templates have the proper functional content.
"""
from django.test import TestCase
from django.core.urlresolvers import reverse

from profile.models import Project


class TestHomeTemplate(TestCase):
    def test_project_site_links_exist(self):
        project1 = Project.objects.create()
        project2 = Project.objects.create(url_to_site='fake_site')

        response = self.client.get(reverse('home'))

        assert 'href="%s"' % 'fake_site' in response.content.decode()
