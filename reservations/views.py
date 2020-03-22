from django.shortcuts import render

from djreservation.views import ProductReservationView
from .models import MyObject


class MyObjectReservation(ProductReservationView):
    base_model = MyObject     # required
    amount_field = 'quantity'  # required
    extra_display_field = ['measurement_unit']  # not required


def reservation(request):
    list_object = MyObject.objects.all()
    import ipdb; ipdb.set_trace()
    return render(request, 'index.html', context={
        'list_object': list_object
    })
