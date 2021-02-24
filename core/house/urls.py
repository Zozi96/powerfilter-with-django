from .views import HouseListView
from django.urls import path

urlpatterns = [
    path('list/', HouseListView.as_view(), name='list-house')
]