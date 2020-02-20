from django.shortcuts import render
from django.views.generic.base import TemplateView

# Homepage class based view 
class HomeView(TemplateView):
    template_name = "index.html"

class LoginView(TemplateView):
    template_name = "login.html"