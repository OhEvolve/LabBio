from django.shortcuts import render

from django.views import generic

from .models import Reagent

# Create your views here.

class ReagentView(generic.DetailView):
    model = Reagent 
    template_name = 'reagents/reagent.html'


