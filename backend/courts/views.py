from django.shortcuts import render
from django.views import generic
from .models import Court
# Создаем представление здесь.

class HomePageView(generic.ListView):
    template_name = 'home.html'
    context_object_name = 'fee' 
    # назначаем список объектов "Court" объекту "fee"
    # передаем объекты "Court", как набор запросов для представления списка
    def get_queryset(self):
        return Court.objects.all()
