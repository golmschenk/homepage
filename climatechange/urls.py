"""
The URL routing for the profile app.
"""
from django.conf.urls import url

from climatechange.views import HomeView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
]
