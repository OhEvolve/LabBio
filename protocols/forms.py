
from django.utils.translation import ugettext_lazy as _

from django import forms
from protocols.models import Step,Protocol,ThermocycleStep

class ProtocolForm(forms.ModelForm):

    class Meta:
        model = Protocol 
        fields = ('date_range',)
        widgets = {
            'date_range': forms.Select(choices=Protocol.CHOICES)
        }


class StepForm(forms.ModelForm):

    class Meta:
        model = Step 
        fields = ('name',)
        widgets = {
            'name': forms.Select(choices=Step.CHOICES)
        }

class ThermocycleForm(forms.ModelForm):

    class Meta:
        model = ThermocycleStep 
        fields = ('stage_type','goto_step','repeats','stage_temp','stage_temp_units','stage_time','stage_time_units')

