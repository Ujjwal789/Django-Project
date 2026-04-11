from django import forms
from .models import chaivarity

class chaivarityForm(forms.ModelForm):
    chai_variety = forms.ModelChoiceField(
        queryset=chaivarity.objects.all(),
        label="Select a chai variety"
    )
    


    class Meta:
        model = chaivarity
        fields = ['chai_variety']

