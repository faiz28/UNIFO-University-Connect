from django.forms import ModelForm
from .models import userinfo

class user_form(ModelForm):
    class Meta:
        model=userinfo
        fields = '__all__'
        exclude = ['user']
        