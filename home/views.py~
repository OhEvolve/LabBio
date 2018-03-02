
from django.views import generic

from reagents.models import Reagent

class OverView(generic.ListView):
    template_name = 'home/home.html'
    context_object_name = 'overview'

    def get_queryset(self):
        return Reagent.objects.order_by('pub_date')

    def get_context_data(self, **kwargs):
        context = super(OverView, self).get_context_data(**kwargs)
        context['reagent_count'] = Reagent.objects.count()
        return context