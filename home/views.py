
from django.views import generic

from reagents.models import Liquid,Solid,Biologic,Solution

class OverView(generic.ListView):
    template_name = 'home/home.html'
    context_object_name = 'overview'

    def get_queryset(self):
        return Liquid.objects.order_by('name')

    def get_context_data(self, **kwargs):
        context = super(OverView, self).get_context_data(**kwargs)
        context['reagent_count'] = sum([obj.objects.count() for obj in (Liquid,Solid,Biologic,Solution)])
        context['liquids'] = Liquid.objects.all()
        context['solids'] = Solid.objects.all()
        context['biologics'] = Biologic.objects.all()
        context['solutions'] = Solution.objects.all()
        return context
