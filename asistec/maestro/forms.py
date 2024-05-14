from django import forms
from .models import Maestro

class MaestroForm(forms.ModelForm):
    class Meta:
        model = Maestro
        fields = "__all__"
