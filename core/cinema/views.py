from django.shortcuts import render
from django.views.generic import TemplateView


class TemplateTest(TemplateView):
    template_name = 'cinema/list.html'
