from django import forms
from .models import event_info

class event_form(forms.ModelForm):
    class Meta:
        model=event_info
        fields = ('__all__')