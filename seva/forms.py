from django import forms
from seva.models import Newreg

class Newregform(forms.ModelForm):
    class Meta:
        model=Newreg
        fields='__all__'

