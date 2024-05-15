from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.views import View
from maestro.models import Maestro
from maestro.forms import MaestroForm

class MaestroListView(View):
    def get(self, request):
        formamaestro = MaestroForm()
        maestros = Maestro.objects.all().order_by("idMaestro")
        return render(request, "indexMaestro.html", {"maestros": maestros, "formamaestro": formamaestro})

class MaestroCreateView(View):
    def post(self, request):
        formamaestro = MaestroForm(request.POST)
        if formamaestro.is_valid():
            formamaestro.save()
            return JsonResponse({'success': True})
        return JsonResponse({'success': False, 'errors': formamaestro.errors})

class MaestroUpdateView(View):
    def get(self, request, id):
        maestro = get_object_or_404(Maestro, pk=id)
        formamaestro = MaestroForm(instance=maestro)
        maestro_html = render_to_string('maestro/EditarMaestro.html', {'formamaestro': formamaestro}, request=request)
        return JsonResponse({'success': True, 'maestro_html': maestro_html, 'maestro': {
            'Nombre': maestro.Nombre,
            'Apellido_Paterno': maestro.Apellido_Paterno,
            'Apellido_Materno': maestro.Apellido_Materno
        }})

    def post(self, request, id):
        maestro = get_object_or_404(Maestro, pk=id)
        formamaestro = MaestroForm(request.POST, instance=maestro)
        if formamaestro.is_valid():
            formamaestro.save()
            return JsonResponse({'success': True})
        return JsonResponse({'success': False, 'errors': formamaestro.errors})

class MaestroDeleteView(View):
    def delete(self, request, id):
        maestro = get_object_or_404(Maestro, pk=id)
        maestro.delete()
        return JsonResponse({'success': True})

nuevoMaestro = MaestroCreateView.as_view()
