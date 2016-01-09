"""
The URL routing for the profile app.
"""
from django.conf.urls import url

from profile.views import Home


urlpatterns = [
    url(r'^$', Home.as_view(), name='home'),
]
