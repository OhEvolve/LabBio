
# source: https://stackoverflow.com/questions/47838059/django-admin-show-hide-fields-if-specific-value-is-selected-in-a-dropdown/47840995#47840995

from django.contrib import admin
from protocols.models import Step,Protocol,ThermocycleStep
from protocols.forms import ProtocolForm,StepForm,ThermocycleForm
from nested_admin import NestedStackedInline,NestedModelAdmin


class ThermocycleInline(NestedStackedInline):

    """ """ 

    fields = (('stage_type','goto_step','repeats'),('stage_temp','stage_temp_units'),('stage_time','stage_time_units'))

    form = ThermocycleForm
    model = ThermocycleStep 
    extra = 1

class StepInline(NestedStackedInline):

    """ """ 

    fields = ('name',('preamble','postamble'),'reagents',('temperature','temperature_units'),('time','time_units'),('speed','speed_units'))

    form = StepForm
    model = Step
    extra = 1

    inlines = [ThermocycleInline]

    class Media:
        js = ('protocols/js/steps.js',)

class ProtocolAdmin(NestedModelAdmin):

    fieldsets = (
        ('Date Range', {
            'fields': ('date_range',),
            'classes': ('predefined',)
        }),
        (None, {
            'fields': (('start_date', 'end_date'),),
            'classes': ('abcdefg',)
        })
    )

    form = ProtocolForm
    inlines = [StepInline]

    class Media:
        js = ('protocols/js/base.js',)

admin.site.register(Protocol,ProtocolAdmin)

