"""
The homepage project admin registration.
"""
from django.contrib import admin

from profile.models import EducationEntry, Essay

admin.site.register(EducationEntry)
admin.site.register(Essay)
