from django import forms
from initiation.models import Name

class NameForm(forms.ModelForm):
    name_value = forms.CharField(max_length=100, help_text = "Enter un nom")

    class Meta:
        model = Name
        fields = ('name_value',)