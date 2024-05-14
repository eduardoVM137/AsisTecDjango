from django.shortcuts import render, redirect, get_object_or_404
from maestro.models import Maestro
from maestro.forms import MaestroForm
from django.http import JsonResponse
from django.template.loader import render_to_string

def nuevoMaestro(request):
    formamaestro = MaestroForm(request.POST or None)
    if formamaestro.is_valid():
        formamaestro.save()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False, 'errors': formamaestro.errors})

def EditarMaestro(request, id):
    maestro = get_object_or_404(Maestro, pk=id)
    if request.method == 'POST':
        formamaestro = MaestroForm(request.POST, instance=maestro)
        if formamaestro.is_valid():
            formamaestro.save()
            return JsonResponse({'success': True})
        return JsonResponse({'success': False, 'errors': formamaestro.errors})
    else:
        formamaestro = MaestroForm(instance=maestro)
        maestro_html = render_to_string('maestro/EditarMaestro.html', {'formamaestro': formamaestro}, request=request)
        return JsonResponse({'success': True, 'maestro_html': maestro_html})

def EliminarMaestro(request, id):
    maestro = get_object_or_404(Maestro, pk=id)
    maestro.delete()
    return redirect("indexmaestro.html")

# views.py en app webapp
def indexMaestro(request):
    formamaestro = MaestroForm()  # Crea una instancia del formulario
    maestros = Maestro.objects.all().order_by("idMaestro")
    return render(request, "indexmaestro.html", {"maestros": maestros, "formamaestro": formamaestro})
