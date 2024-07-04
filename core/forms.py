#Form for the City model

from django import forms
from .models import City

class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ('name', 'state', 'country')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'name': 'City Name',
            'state': 'State',
            'country': 'Country',
        }
        