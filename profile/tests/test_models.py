"""
Tests for the models.
"""
from django.test import TestCase

from profile.models import Essay, EducationEntry


class TestEssay(TestCase):
    def test_title_can_be_saved(self):
        essay = Essay()
        title = 'An Awesome Title'

        essay.title = title
        essay.save()
        saved_essay = Essay.objects.first()

        assert saved_essay.title == title

    def test_slug_is_automatically_save_from_title(self):
        essay = Essay()
        title = 'An Awesome Title'

        essay.title = title
        essay.save()
        saved_essay = Essay.objects.first()

        assert saved_essay.slug == 'an-awesome-title'


class TestEducationEntry(TestCase):
    def test_education_entry_can_save_content(self):
        education_entry = EducationEntry()
        degree = "Degree content"

        education_entry.degree = degree
        education_entry.save()
        saved_education_entry = EducationEntry.objects.first()

        assert saved_education_entry.degree == degree

    def test_graduation_date_can_be_saved_empty(self):
        education_entry = EducationEntry(graduation_date=None)

        education_entry.save()
        saved_education_entry = EducationEntry.objects.first()

        assert saved_education_entry.graduation_date is None
