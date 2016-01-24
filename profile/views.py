from django.views.generic import TemplateView

from profile.models import Essay as EssayModel


class Home(TemplateView):
    template_name = 'home.html'

    def get_context_data(self):
        context = {}
        context['essays'] = EssayModel.objects.all()
        return context


class Essay(TemplateView):
    template_name = 'essay.html'

