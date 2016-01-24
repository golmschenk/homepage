from django.views.generic import TemplateView, DetailView

from profile import models


class Home(TemplateView):
    template_name = 'profile/home.html'

    def get_context_data(self):
        context = {}
        context['essays'] = models.Essay.objects.all()
        return context


class Essay(DetailView):
    model = models.Essay

