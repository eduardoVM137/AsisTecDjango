from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.views import View
from asistencia.models import Asistencia
from asistencia.forms import AsistenciaForm

class AsistenciaListView(View):
    def get(self, request):
        formaAsistencia = AsistenciaForm()
        asistencias = Asistencia.objects.all().order_by("idAsistencia")
        return render(request, "indexAsistencia.html", {"asistencias": asistencias, "formaasistencia": formaAsistencia})