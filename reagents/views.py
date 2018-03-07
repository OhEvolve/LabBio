from django.shortcuts import render

from django.views import generic

from .models import Liquid,Solid,Biologic,Solution 

# Create your views here.

class LiquidView(generic.DetailView):
    model = Liquid 
    template_name = 'reagents/liquid.html'

class SolidView(generic.DetailView):
    model = Solid 
    template_name = 'reagents/solid.html'

class BiologicView(generic.DetailView):
    model = Biologic 
    template_name = 'reagents/biologic.html'

class SolutionView(generic.DetailView):
    model = Solution 
    template_name = 'reagents/solution.html'


