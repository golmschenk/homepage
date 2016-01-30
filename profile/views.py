"""
Views for the app.
"""
from django.views.generic import TemplateView, DetailView

from profile.models import Essay, EducationEntry


class HomeView(TemplateView):
    """
    The home view to be displayed for the landing page.
    """
    template_name = 'profile/home.html'

    def get_context_data(self):
        """
        Generates the context for the view.
        """
        context = {
            'essays': Essay.objects.all(),
            'education_entries': EducationEntry.objects.all()
        }
        return context


class EssayView(DetailView):
    """
    The view to display essay information.
    """
    model = Essay

