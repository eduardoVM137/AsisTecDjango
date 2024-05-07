from django.forms import ModelForm, EmailInput
from maestro.models import Maestro
class MaestroForm(ModelForm):
 class Meta:
  model = Maestro
  fields = "__all__"