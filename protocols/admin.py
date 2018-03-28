
# source: https://stackoverflow.com/questions/47838059/django-admin-show-hide-fields-if-specific-value-is-selected-in-a-dropdown/47840995#47840995

from django.contrib import admin
from protocols.models import Step,Protocol,OperateStep,ThermocycleStep,Input,Output
from protocols.forms import ProtocolForm,StepForm,OperateForm,ThermocycleForm,InputForm,OutputForm
from nested_admin import NestedStackedInline,NestedTabularInline,NestedModelAdmin
from .models import Step


class OperateInline(NestedStackedInline):

    """ """ 

    fields = ('description',)

    form = OperateForm
    model = OperateStep 
    extra = 0

class ThermocycleInline(NestedStackedInline):

    """ """ 

    fields = (('stage_type','goto_step','repeats'),('stage_temp','stage_temp_units'),('stage_time','stage_time_units'))

    form = ThermocycleForm
    model = ThermocycleStep 
    extra = 0

""" Liquid Content """
class LiquidContentInlineAdmin(NestedTabularInline):
    model = Step.liquids.through
    extra,min_num = 0,0 
    #fk_name = 'liquid_to_solution'

""" Solid Content """
class SolidContentInlineAdmin(NestedTabularInline):
    model = Step.solids.through
    extra,min_num = 0,0 
    #fk_name = 'solid_to_solution'

""" Biologic Content """
class BiologicContentInlineAdmin(NestedTabularInline):
    model = Step.biologics.through
    extra,min_num = 0,0 
    #fk_name = 'biologic_to_solution'

class CellContentInlineAdmin(NestedTabularInline):
    model = Step.cells.through
    extra,min_num = 0,0 
    #fk_name = 'biologic_to_solution'


class InputInline(NestedTabularInline):

    form = InputForm
    model = Input
    extra = 0

class OutputInline(NestedTabularInline):

    form = OutputForm
    model = Output
    extra = 0

class StepInline(NestedStackedInline):

    """ """ 

    fields = (('name','defined_through_inputs'),('preamble','postamble'),('temperature','temperature_units'),('time','time_units'),('speed','speed_units'),'container','action')

    form = StepForm
    model = Step
    extra = 1

    inlines = [
            ThermocycleInline,
            OperateInline,
            LiquidContentInlineAdmin,
            SolidContentInlineAdmin,
            BiologicContentInlineAdmin,
            CellContentInlineAdmin
            ]

    class Media:
        js = ('protocols/js/steps.js',)

class ProtocolAdmin(NestedModelAdmin):

    fieldsets = (
        ('Overview', {
            'fields': ('IO_template',),
            'classes': ('predefined',)
        }),
        (None, {
            'fields': ((),),
            'classes': ('abcdefg',)
        })
    )

    form = ProtocolForm
    inlines = [InputInline,OutputInline,StepInline]

    class Media:
        js = ('protocols/js/base.js',)


admin.site.register(Protocol,ProtocolAdmin)

