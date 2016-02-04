"""
Tests for the models.
"""
from datetime import date
from django.test import TestCase

from profile.models import Essay, EducationEntry, TeachingEntry


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


class TestTeachingEntry(TestCase):
    def test_teaching_entry_can_save_content(self):
        teaching_entry = TeachingEntry()
        course_number = "CSC 0000"

        teaching_entry.course_number = course_number
        teaching_entry.save()
        saved_teaching_entry = TeachingEntry.objects.first()

        assert saved_teaching_entry.course_number == course_number

    def test_term_gives_season_name_of_fall_for_the_fall_date_range(self):
        teaching_entry = TeachingEntry()
        teaching_entry.start_date = date(2014, 8, 28)
        teaching_entry.end_date = date(2014, 12, 23)

        assert teaching_entry.term == 'Fall'
