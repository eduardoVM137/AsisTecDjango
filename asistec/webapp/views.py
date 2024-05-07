from django.shortcuts import render, redirect, get_object_or_404
from maestro.models import Maestro
from salon.models import Salon
from materia.models import Materia
from horario_salon.models import Horario_Salon
from asistencia.models import Asistencia

from maestro.forms import MaestroForm

# Create your views here.
def indexMaestro(request):
 maestros = Maestro.objects.order_by("idMaestro")
 return render(request, "indexMaestro.html", 
 {"maestro": maestros})

def index(request):
 maestros = Maestro.objects.order_by("idMaestro")
 return render(request, "indexMaestro.html", 
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

def nuevoMaestro(request):
    if request.method == "POST":
        formamaestro = MaestroForm(request.POST)
        if formamaestro.is_valid():
            formamaestro.save()
            return redirect("ListadoMaestros")
        else:
            formamaestro = MaestroForm()
            return render(request, "../maestro/Agregar.html", {"formamaestro": formamaestro})


 