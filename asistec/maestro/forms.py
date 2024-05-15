from django import forms
from maestro.models import Maestro

class MaestroForm(forms.ModelForm):
    class Meta:
        model = Maestro
        fields = '__all__'
