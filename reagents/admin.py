
from django.contrib import admin

from .models import Reagent



class ReagentAdmin(admin.ModelAdmin):

    fieldsets = [
        (None, {'fields': ['name','mw','pub_date']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
        ]



admin.site.register(Reagent, ReagentAdmin)
