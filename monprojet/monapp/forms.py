from django import forms
from .models import Pays, Region

class PaysForm(forms.ModelForm):
    class Meta:
        model =Pays
        fields = '__all__'

class RegionForm(forms.ModelForm):
    class Meta:
        model = Region
        fields = '__all__'