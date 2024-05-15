from django.shortcuts import render, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from maestro.models import Maestro
from maestro.forms import MaestroForm
from salon.models import Salon
from materia.models import Materia
from horario_salon.models import Horario_Salon
from asistencia.models import Asistencia


class IndexView(View):
    def get(self, request):
        return render(request, "webapp/index.html")

class MaestroListView(LoginRequiredMixin, View):
    def get(self, request):
        formamaestro = MaestroForm()
        maestros = Maestro.objects.all().order_by("idMaestro")
        return render(request, "indexmaestro.html", {"maestros": maestros, "formamaestro": formamaestro})

class SalonListView(LoginRequiredMixin, View):
    def get(self, request):
        salones = Salon.objects.order_by("idSalon")
        return render(request, "indexSalon.html", {"salones": salones})

class HorarioSalonListView(LoginRequiredMixin, View):
    def get(self, request):
        horario_salones = Horario_Salon.objects.order_by("idHorario")
        return render(request, "indexHorario_Salon.html", {"horario_salones": horario_salones})

class AsistenciaListView(LoginRequiredMixin, View):
    def get(self, request):
        asistencias = Asistencia.objects.order_by("idAsistencia")
        return render(request, "indexAsistencia.html", {"asistencias": asistencias})

class MateriaListView(LoginRequiredMixin, View):
    def get(self, request):
        materias = Materia.objects.order_by("idMateria")
        return render(request, "indexMateria.html", {"materias": materias})
