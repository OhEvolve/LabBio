
from django.contrib import admin

from .models import Liquid,Solid,Biologic,Cell,Solution



class LiquidAdmin(admin.ModelAdmin):

    fieldsets = [
        (None, {'fields': ['name','owner']}),
        ]

class SolidAdmin(admin.ModelAdmin):

    fieldsets = [
        (None, {'fields': ['name','owner',('mw','mw_units')]}),
        ]
        
class BiologicAdmin(admin.ModelAdmin):

    fieldsets = [
        (None, {'fields': ['name','owner','sequence','form','shape','material']}),
        ]


""" Liquid Content """
class LiquidContentInlineAdmin(admin.TabularInline):
    model = Solution.liquids.through
    extra,min_num = 0,1 
    #fk_name = 'liquid_to_solution'

""" Solid Content """
class SolidContentInlineAdmin(admin.TabularInline):
    model = Solution.solids.through
    extra,min_num = 1,0 
    #fk_name = 'solid_to_solution'

""" Biologic Content """
class BiologicContentInlineAdmin(admin.TabularInline):
    model = Solution.biologics.through
    extra,min_num = 1,0 
    #fk_name = 'biologic_to_solution'

""" Cell-Biologic Content """
class CellBiologicContentInlineAdmin(admin.TabularInline):
    model = Cell.biologics.through
    extra,min_num = 1,0 
    #fk_name = 'biologic_to_solution'


class CellAdmin(admin.ModelAdmin):

    fieldsets = [
        (None, {'fields': ['name','owner','shaken','media_preference','morphology',('doubling_time','doubling_time_units'),'culture_environment']}),
        ]

    inlines = (CellBiologicContentInlineAdmin,)

class SolutionAdmin(admin.ModelAdmin):

    fieldsets = [
        (None, {'fields': ['name','owner']}),
        ]

    inlines = (LiquidContentInlineAdmin,
               SolidContentInlineAdmin,
               BiologicContentInlineAdmin)



        

admin.site.register(Liquid, 	LiquidAdmin)
admin.site.register(Solid,       SolidAdmin)
admin.site.register(Biologic, BiologicAdmin)
admin.site.register(Cell,         CellAdmin)
admin.site.register(Solution, SolutionAdmin)



