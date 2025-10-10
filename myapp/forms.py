from django import forms
from .models import Table
from django.core.exceptions import ValidationError

class TableForm(forms.ModelForm):
    class Meta:
        model = Table
        fields = ['name', 'age', 'email', 'address','image','video']

    