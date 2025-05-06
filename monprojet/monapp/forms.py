from django import forms
from .models import Pays, Region

class PaysForm(forms.ModelForm):
    class Meta:
        model = Pays
        fields = '__all__'

class RegionForm(forms.ModelForm):
    class Meta:
        model = Region
        fields = ['pays','region','ville', 'superficie', 'population']

    pays = forms.ModelChoiceField(queryset=Pays.objects.all(), empty_label="Choisir un pays")