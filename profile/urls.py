"""
The URL routing for the profile app.
"""
from django.conf.urls import url

from profile.views import Home


urlpatterns = [
    url(r'^$', Home.as_view(), name='home'),
    url(r'^essay/(?P<url_title>[\w-]+)$', Home.as_view(), name='essay'),
]
