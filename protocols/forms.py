
from django.utils.translation import ugettext_lazy as _

from django import forms
from protocols.models import Step,Protocol,OperateStep,ThermocycleStep

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
        fields = ('stage_type',)
        widgets = {
            'stage_type': forms.Select(choices=Step.CHOICES)
        }

class OperateForm(forms.ModelForm):

    class Meta:
        model = OperateStep 
        fields = ('description',)
