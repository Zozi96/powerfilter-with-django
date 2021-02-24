from django.views.generic.list import ListView
from .models import House
from .filters import HouseFilter


class HouseListView(ListView):
    model = House
    template_name = 'house/list.html'

    def get_queryset(self):
        qs = self.model.objects.all()
        house_list = HouseFilter(self.request.GET, queryset=qs)
        return house_list.qs

    def get_context_data(self, **kwargs):
        context = super(HouseListView, self).get_context_data(**kwargs)
        context['title'] = 'Lista de casas'
        return context
