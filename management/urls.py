from django.urls import path, include 
from . import views
<<<<<<< HEAD
from .views import CarWashReservation
=======
>>>>>>> d3bfcdbf8821f64d0e69c97ba88df0a45d59d1ff
from django.views.generic import TemplateView


urlpatterns = [
    path('', TemplateView.as_view(template_name="home.html"), name="home"),
    path('signup/', views.SignUpView.as_view(), name="signup"),
    path('accounts/', include('django.contrib.auth.urls')),
<<<<<<< HEAD
    path('profile/', TemplateView.as_view(template_name="profile.html"), name="profile"),
=======
>>>>>>> d3bfcdbf8821f64d0e69c97ba88df0a45d59d1ff
    
]
