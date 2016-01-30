"""
The URL routing for the profile app.
"""
from django.conf.urls import url

from profile.views import HomeView, EssayView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^essay/(?P<slug>[\w-]+)$', EssayView.as_view(), name='essay'),
]
