from django.shortcuts import render

from djreservation.views import ProductReservationView
from .models import MyObject


class MyObjectReservation(ProductReservationView):
    base_model = MyObject     # required
    amount_field = 'quantity'  # required
    extra_display_field = ['measurement_unit']  # not required


def reserve(request):
    list_object = MyObject.objects.all()
    return render(request, 'reserve.html', context={
        'list_object': list_object
    })
