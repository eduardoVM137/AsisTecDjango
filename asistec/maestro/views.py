 
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

   return render(request, "./EditarMaestro.html", {"formamaestro": formaMaestro})