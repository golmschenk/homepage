from unittest.mock import patch

from django.core.urlresolvers import reverse, resolve
from django.test import TestCase


class TestUrlNames(TestCase):
    @patch('profile.views.Home')
    def test_home_url_routes_to_home_view(self, mock_home_view):
        url = reverse('home')
        match = resolve(url)

        assert match.func == mock_home_view.as_view()

    @patch('profile.views.Essay')
    def test_essay_url_name_routes_to_essay_view(self, mock_essay_view):
        url = reverse('essay', kwargs={'url_title': 'url_title'})
        match = resolve(url)

        assert match.func == mock_essay_view.as_view()
