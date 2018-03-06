
from django.contrib import admin

from .models import Liquid,Solid,Biologic,Solution



class LiquidAdmin(admin.ModelAdmin):

    fieldsets = [
        (None, {'fields': ['name','owner']}),
        ]

class SolidAdmin(admin.ModelAdmin):

    fieldsets = [
        (None, {'fields': ['name','owner','mw']}),
        ]
        
class BiologicAdmin(admin.ModelAdmin):

    fieldsets = [
        (None, {'fields': ['name','owner','sequence','form','shape','material']}),
        ]


# may not be best expression here
class TermInlineAdmin(admin.TabularInline):
    model = Solution.liquids.through


class SolutionAdmin(admin.ModelAdmin):

    fieldsets = [
        (None, {'fields': ['name','owner']}),
        ]

    inlines = (TermInlineAdmin,) 
        

admin.site.register(Liquid, 	  LiquidAdmin)
admin.site.register(Solid, 	   SolidAdmin)
admin.site.register(Biologic, BiologicAdmin)
admin.site.register(Solution, SolutionAdmin)
