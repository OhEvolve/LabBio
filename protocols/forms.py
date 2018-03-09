

from django import forms
from protocols.models import Step,Protocol 

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
        fields = ('date_range',)
        widgets = {
            'date_range': forms.Select(choices=Step.CHOICES)
        }
