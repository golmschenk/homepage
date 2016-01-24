"""
The URL routing for the profile app.
"""
from django.conf.urls import url

from profile.views import Home, Essay

urlpatterns = [
    url(r'^$', Home.as_view(), name='home'),
    url(r'^essay/(?P<slug>[\w-]+)$', Essay.as_view(), name='essay'),
]
