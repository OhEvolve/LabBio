# home/tables.py

import django_tables2 as tables
from reagents.models import Liquid,Solid,Biologic,Solution


class LiquidTable(tables.Table):
    class Meta:
        model = Liquid
        template_name = 'django_tables2/bootstrap.html'

class SolidTable(tables.Table):
    class Meta:
        model = Solid 
        template_name = 'django_tables2/bootstrap.html'

class BiologicTable(tables.Table):
    class Meta:
        model = Biologic 
        template_name = 'django_tables2/bootstrap.html'
        fields = ('id','name','owner','form','material','shape')

class SolutionTable(tables.Table):
    class Meta:
        model = Solution 
        template_name = 'django_tables2/bootstrap.html'
