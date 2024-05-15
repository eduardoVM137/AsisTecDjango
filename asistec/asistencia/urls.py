from django.urls import path
from .views import AsistenciaListView

urlpatterns = [
    path('', AsistenciaListView.as_view(), name='listado_asistencia'), 
]
