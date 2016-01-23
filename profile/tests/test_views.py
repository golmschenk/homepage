from unittest.mock import patch, Mock

from django.test import TestCase

from profile.views import Home


class TestHomeView(TestCase):

    @patch('profile.views.Home.get_context_data')
    def test_front_page_renders_home_template(self, _):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    @patch('profile.views.Essay')
    def test_get_context_data_adds_essays_to_context(self, mock_essay_class):
        mock_essay_class.objects.all = Mock(return_value='essay list')
        home_view = Home()

        context = home_view.get_context_data()

        assert context['essays'] == 'essay list'



