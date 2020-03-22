from django.urls import path, include 
from . import views
from .views import CarWashReservation
from django.views.generic import TemplateView
from djreservation import urls as djreservation_urls

urlpatterns = [
    path('', TemplateView.as_view(template_name="index.html"), name="home"),
    path('signup/', views.SignUpView.as_view(), name="signup"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('profile/', TemplateView.as_view(template_name="profile.html"), name="profile"),
    path(r"^reservationroom/create/)$", CarWashReservation.as_view(), name='create_reservation')
]
urlpatterns += djreservation_urls.urlpatterns