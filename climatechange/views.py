"""
Views for the app.
"""
from django.views.generic import TemplateView

class HomeView(TemplateView):
    """
    The home view to be displayed for the landing page.
    """
    template_name = 'climatechange/home.html'
