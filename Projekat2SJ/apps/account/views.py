from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin



class ProfileView(TemplateView):
    template_name = 'accounts/profile.html'

