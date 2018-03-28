
from django.utils.translation import ugettext_lazy as _

from django import forms
from protocols.models import Step,Protocol,OperateStep,ThermocycleStep,Input,Output

class ProtocolForm(forms.ModelForm):

    class Meta:
        model = Protocol 
        fields = ('IO_template',)
        widgets = {
            'IO_template': forms.Select(choices=Protocol.CHOICES)
        }

class StepForm(forms.ModelForm):

    class Meta:
        model = Step 
        fields = ('name',)
        widgets = {
            'name': forms.Select(choices=Step.CHOICES)
        }

class InputForm(forms.ModelForm):

    class Meta:
        model = Input
        fields = ('input_type','minimum_entries','maximum_entries')

class OutputForm(forms.ModelForm):

    class Meta:
        model = Output
        fields = ('output_type','minimum_entries','maximum_entries')

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
