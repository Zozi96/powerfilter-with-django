from django_filters.views import FilterView

from .filters import CineFilter


class TemplateTest(FilterView):
    filterset_class = CineFilter
    template_name = 'cinema/list.html'
