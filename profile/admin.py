"""
The homepage project admin registration.
"""
from django.contrib import admin

from profile.models import EducationEntry, Essay, TeachingEntry

admin.site.register(EducationEntry)
admin.site.register(Essay)
admin.site.register(TeachingEntry)
