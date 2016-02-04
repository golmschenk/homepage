"""
The models for the app.
"""
from datetime import date
from django.db import models
from django.utils.text import slugify


class EducationEntry(models.Model):
    """
    A model to store data about education records.
    """
    degree = models.TextField(default='')
    graduation_date = models.DateField(null=True, blank=True)
    additional_information = models.TextField(default='')


class Essay(models.Model):
    """
    A model for storing data about written articles and essays.
    """
    title = models.TextField(default='')
    slug = models.SlugField(default='')
    url_of_original_article = models.URLField(default='')
    publisher = models.TextField(default='')
    issue = models.TextField(default='')
    publication_date = models.DateField(blank=True, null=True)
    body = models.TextField(default='')

    def save(self, *args, **kwargs):
        """
        Saving capabilities for the essay model.
        """
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class TeachingEntry(models.Model):
    """
    A model for storing information about courses taught.
    """
    course_number = models.TextField(default='')
    title = models.TextField(default='')
    school = models.TextField(default='')
    position = models.TextField(default='')
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    @property
    def term(self):
        """
        Gets the string of the term name for the date range of the teaching entry.

        :return: The name of the term.
        :rtype: str
        """
        if self.start_date < date(self.start_date.year, 10, 1) < self.end_date:
            return "Fall"
