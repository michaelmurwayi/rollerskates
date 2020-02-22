from django.urls import path, include 
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name="index.html"), name="home"),
    path('signup/', views.SignUpView.as_view(), name="signup"),
    path('accounts/', include('django.contrib.auth.urls')),
]