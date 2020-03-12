from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

class HomeView(TemplateView):
    template_name = "index.html"
    
class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('accounts/')
    template_name = "signup.html"

    def post(self, request):
        form = self.form_class(request.post)
        
        if form.is_valid():
            return HttpResponseRedirect('/admin/')

            return render(request, self.template_name, {'form': form})