from django import forms
from .models import achievment_list

class achievement_form(forms.ModelForm):
    class Meta:
        model=achievment_list
        fields = ('__all__')