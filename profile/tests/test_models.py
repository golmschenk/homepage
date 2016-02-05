"""
Tests for the models.
"""
from datetime import date
from django.test import TestCase

from profile.models import Essay, EducationEntry, Project, TeachingEntry


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

    def test_term_gives_season_name_of_spring_for_the_spring_date_range(self):
        teaching_entry = TeachingEntry()
        teaching_entry.start_date = date(2016, 1, 29)
        teaching_entry.end_date = date(2016, 5, 28)

        assert teaching_entry.term == 'Spring'

    def test_aggregation_of_the_same_course_over_different_semesters(self):
        teaching_entry1 = TeachingEntry(course_number="CSC 0000")
        teaching_entry2 = TeachingEntry(course_number="CSC 1111")
        teaching_entry3 = TeachingEntry(course_number="CSC 0000")
        teaching_entry1.save()
        teaching_entry2.save()
        teaching_entry3.save()

        aggregated_teaching_entries = TeachingEntry.attain_aggregated()

        assert len(aggregated_teaching_entries) == 2
        assert aggregated_teaching_entries["CSC 0000"] == [teaching_entry1, teaching_entry3]
        assert aggregated_teaching_entries["CSC 1111"] == [teaching_entry2]


class TestProject(TestCase):
    def test_project_can_save_content(self):
        project = Project()
        title = "An Awesome Project"

        project.title = title
        project.save()
        saved_project = Project.objects.first()

        assert saved_project.title == title
