from django import forms
import django_filters as filters
from .models import House, Characteristic

characteristics = Characteristic.objects.all()


class HouseFilter(filters.FilterSet):
    characteristichouse__characteristics = filters.ModelMultipleChoiceFilter(
        label='Caracteristicas', queryset=characteristics, widget=forms.CheckboxSelectMultiple)
    cost__cost_of_sale = filters.NumberFilter(label='Precio de venta', widget=forms.NumberInput())
    cost__rental_cost = filters.NumberFilter(label='Precio de renta', widget=forms.NumberInput())

    class Meta:
        model = House
        fields = [
            'title',
            'characteristichouse__characteristics',
            'cost__cost_of_sale',
            'cost__rental_cost',
        ]
