from unittest.mock import patch, Mock

from django.test import TestCase

from profile.views import Home, Essay


class TestHomeView(TestCase):

    def test_front_page_renders_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    @patch('profile.views.EssayModel')
    def test_get_context_data_adds_essays_to_context(self, mock_essay_class):
        mock_essay_class.objects.all = Mock(return_value='essay list')
        home_view = Home()

        context = home_view.get_context_data()

        assert context['essays'] == 'essay list'


class TestEssayView(TestCase):
    pass


