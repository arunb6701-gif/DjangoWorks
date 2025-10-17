
from  django import forms
from app1.models import Moviedetail

class Movieform(forms.ModelForm):
    class Meta:
        model=Moviedetail
        fields='__all__'
