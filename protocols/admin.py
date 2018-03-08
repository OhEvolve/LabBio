
# source: https://stackoverflow.com/questions/47838059/django-admin-show-hide-fields-if-specific-value-is-selected-in-a-dropdown/47840995#47840995

from django.contrib import admin
from protocols.models import Step,Protocol
from protocols.forms import ProtocolForm,StepForm

class StepInline(admin.TabularInline):

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

    form = StepForm
    model = Step
    extra = 3

    class Media:
        js = ('protocols/js/steps.js',)

class ProtocolAdmin(admin.ModelAdmin):

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

