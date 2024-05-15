from django import forms
from asistencia.models import Asistencia

class AsistenciaForm(forms.ModelForm):
    class Meta:
        model = Asistencia
        fields = '__all__'
