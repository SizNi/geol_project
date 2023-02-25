from django.views.generic import TemplateView
from django.utils.translation import gettext_lazy as _


class Index(TemplateView):

    template_name = 'index.html'
