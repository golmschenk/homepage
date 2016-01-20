from django.test import TestCase

from profile.models import Essay


class TestEssay(TestCase):
    def test_title_can_be_saved(self):
        essay = Essay()
        title = 'An Awesome Title'

        essay.title = title
        essay.save()
        saved_essay = Essay.objects.first()

        assert saved_essay.title == title

    def test_url_title_is_a_property_that_returns_hyphenized_title(self):
        essay = Essay()
        title = 'An Awesome Title'
        essay.title = title

        url_title = essay.url_title

        assert url_title == 'an-awesome-title'
