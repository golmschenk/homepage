from django.views.generic import TemplateView

from profile.models import Essay


class Home(TemplateView):
    template_name = 'home.html'

    def get_context_data(self):
        context = {}
        context['essays'] = Essay.objects.all()
        return context
