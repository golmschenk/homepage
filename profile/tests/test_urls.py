from unittest.mock import patch

from django.core.urlresolvers import reverse, resolve
from django.test import TestCase


class TestUrlNames(TestCase):
    @patch('profile.urls.Home')
    def test_home_url_routes_to_home_view(self, mock_home_view):
        url = reverse('home')

        assert url == '/'
