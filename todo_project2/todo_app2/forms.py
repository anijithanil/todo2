from . models import Todoapp
from django import forms

class Todoform(forms.ModelForm):
    class Meta:
        model=Todoapp
        fields=['name','priority','date']