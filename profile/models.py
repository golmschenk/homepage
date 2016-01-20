from django.db import models


class Essay(models.Model):
    """
    A model for storing data about written articles and essays.
    """
    title = models.TextField(default='')

