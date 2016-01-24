"""
Views for the app.
"""
from django.views.generic import TemplateView, DetailView

from profile import models


class Home(TemplateView):
    """
    The home view to be displayed for the landing page.
    """
    template_name = 'profile/home.html'

    def get_context_data(self):
        """
        Generates the context for the view.
        """
        context = {'essays': models.Essay.objects.all()}
        return context


class Essay(DetailView):
    """
    The view to display essay information.
    """
    model = models.Essay

