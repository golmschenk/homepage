from django.db import models
from django.utils.text import slugify


class Essay(models.Model):
    """
    A model for storing data about written articles and essays.
    """
    title = models.TextField(default='')
    slug = models.SlugField(default='')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
