from django import forms
import django_filters as filters
from .models import House, Characteristic

characteristics = Characteristic.objects.all()


class HouseFilter(filters.FilterSet):
    characteristichouse__characteristics = filters.ModelMultipleChoiceFilter(
        queryset=characteristics, widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = House
        fields = [
            'title',
            'description',
            'characteristichouse__characteristics',
            'cost__cost_of_sale',
            'cost__rental_cost',
        ]
