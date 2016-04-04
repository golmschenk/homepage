"""
The homepage project admin registration.
"""
from django.contrib import admin

from profile.models import EducationEntry, Essay, TeachingEntry, Project

admin.site.register(EducationEntry)
admin.site.register(Essay)
admin.site.register(Project)
admin.site.register(TeachingEntry)
