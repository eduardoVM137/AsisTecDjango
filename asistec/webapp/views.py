from django.shortcuts import render, redirect, get_object_or_404
from maestro.models import Maestro
from maestro.forms import MaestroForm


from salon.models import Salon
from materia.models import Materia
from horario_salon.models import Horario_Salon
from asistencia.models import Asistencia


# Create your views here.

def indexMaestro(request):
    formamaestro = MaestroForm()  # Crea una instancia del formulario
    maestros = Maestro.objects.all().order_by("idMaestro")
    return render(request, "indexMaestro.html", {"maestros": maestros, "formamaestro": formamaestro})



def index(request):
 maestros = Maestro.objects.order_by("idMaestro")
 return render(request, "index.html", 
 {"maestro": maestros})



def salon(request):
 salones = Salon.objects.order_by("idSalon")
 return render(request, "indexSalon.html", 
 {"salones": salones})

def horario_salon(request):
 Horario_Salones = Horario_Salon.objects.order_by("idHorario")
 return render(request, "indexHorario_Salon.html", 
 {"horario_salones": Horario_Salones})

def asistencia(request):
 asistencias = Asistencia.objects.order_by("idAsistencia")
 return render(request, "indexAsistencia.html", 
 {"asistencias": asistencias})

def materia(request):
 materias = Materia.objects.order_by("idMateria")
 return render(request, "indexMateria.html", 
 {"materias": materias})
