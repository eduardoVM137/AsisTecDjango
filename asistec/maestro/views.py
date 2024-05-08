 
from django.shortcuts import render, redirect, get_object_or_404
from maestro.models import Maestro
from maestro.forms import MaestroForm

# Create your views here.


def EliminarMaestro(request, id):
 maestro = get_object_or_404(Maestro, pk=id)
 if maestro:
    maestro.delete()
 return redirect("ListadoMaestros")

def EditarMaestro(request, id):
   maestro = get_object_or_404(Maestro, pk=id)
   if request.method == "POST":
      formaMaestro = MaestroForm(request.POST, instance=maestro)
      if formaMaestro.is_valid(): 
         formaMaestro.save()
         return redirect("ListadoMaestros")
   else:
      formaMaestro = MaestroForm(instance=maestro) 
   return render(request, "maestro/EditarMaestro.html", {"formamaestro": formaMaestro})


def DetalleMaestro(request, idMaestro):
 maestro = get_object_or_404(Maestro, pk=idMaestro)
 print(maestro.Apellido_Materno)
 return render(request, "maestro/detalleMaestro.html", {"maestro": maestro})



def nuevoMaestro(request):
    if request.method == "POST":
        formamaestro = MaestroForm(request.POST)
        if formamaestro.is_valid():
            formamaestro.save()
            return redirect("ListadoMaestros")
    else:
        formamaestro = MaestroForm()
    print("kola")    
    return render(request, "maestro/Agregar.html", {"formamaestro": formamaestro})
        
