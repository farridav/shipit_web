from django.views.generic import TemplateView

from .models import ContactForm


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'food': 'cheese',
            'messages': ContactForm.objects.all()
        })
        return context
