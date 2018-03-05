
from django.views import generic

from reagents.models import Liquid,Solid,Biologic,Solution
from home.tables import LiquidTable,SolidTable,BiologicTable,SolutionTable

class OverView(generic.ListView):
    template_name = 'home/home.html'
    context_object_name = 'overview'

    def get_queryset(self):
        return Liquid.objects.order_by('name')

    def get_context_data(self, **kwargs):
        context = super(OverView, self).get_context_data(**kwargs)
        context['reagent_count'] = sum([obj.objects.count() for obj in (Liquid,Solid,Biologic,Solution)])
        # add reagent references (probably not necessary, just need counts)
        context['liquids'] = Liquid.objects.all()
        context['solids'] = Solid.objects.all()
        context['biologics'] = Biologic.objects.all()
        context['solutions'] = Solution.objects.all()
        # generate content tables
        context['table_liquids'] =  LiquidTable(Liquid.objects.all(), prefix="1-")
        context['table_solids'] =  SolidTable(Solid.objects.all(), prefix="2-")
        context['table_biologics'] =  BiologicTable(Biologic.objects.all(), prefix="3-")
        context['table_solutions'] =  SolutionTable(Solution.objects.all(), prefix="4-")
        # return modified context
        return context

""" Intercept Tables and apply standardized format """
def reagents_listings(request):
    table = LiquidTable(Liquid.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'default_table.html', {'table': table})
