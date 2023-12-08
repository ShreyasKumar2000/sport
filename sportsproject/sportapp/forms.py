from django import forms
from . models import Football

class FootballForm(forms.ModelForm):
    class Meta:
        model=Football
        fields=['name','desc','club','bdor','img']