from django.test import TestCase

from profile.models import Essay


class TestEssay(TestCase):
    def test_essay_title_can_be_saved(self):
        essay = Essay()
        title = 'An Awesome Title'

        essay.title = title
        essay.save()
        saved_essay = Essay.objects.first()

        assert saved_essay.title == title