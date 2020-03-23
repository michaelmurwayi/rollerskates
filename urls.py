"""demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from djreservation import urls as djreservation_urls
<<<<<<< HEAD
from demoapp.views import home, MyObjectReservation

urlpatterns = [
    path('reserve/', home, name="reserve"),
=======
from reservations.views import reservation, MyObjectReservation

urlpatterns = [
    path('profile', reservation, name='profile'),
>>>>>>> d3bfcdbf8821f64d0e69c97ba88df0a45d59d1ff
    path('admin/', admin.site.urls),
    re_path(r"^reservation/create/(?P<modelpk>\d+)$",
            MyObjectReservation.as_view(), name="myreservation"),
    path('', include("management.urls"))
] + djreservation_urls.urlpatterns
