import django_filters as filters
from django import forms
from .models import Cine


class CineFilter(filters.FilterSet):
    name = filters.CharFilter(label='Cine', lookup_expr='icontains')
    movie__name = filters.CharFilter(label='Nombre de la pelicula', lookup_expr='icontains')
    movie__hour = filters.TimeFilter(label='Hora de la función', lookup_expr='icontains')

    class Meta:
        model = Cine
        fields = [
            'name',
            'movie__name',
            'movie__hour',
        ]
